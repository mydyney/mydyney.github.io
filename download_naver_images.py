#!/usr/bin/env python3
"""
네이버 블로그 이미지 다운로드 스크립트 (광고 자동 제거)

기능:
    1. 네이버 블로그 광고 블록 자동 제거
       - ad_power_content_wrap
       - ssp-adcontent
       - data-ad 속성
    2. 실제 콘텐츠 이미지만 추출 및 다운로드
    3. JPG 형식으로 변환 및 최적화
    4. 중복 이미지 자동 제거

사용법:
    python3 download_naver_images.py <HTML파일경로> <포스트슬러그>

예시:
    python3 download_naver_images.py naver_blog.html kirimugiya-jinroku

출력:
    - static/images/posts/{slug}-01.jpg
    - static/images/posts/{slug}-02.jpg
    - ...
"""

import re
import os
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse, unquote
from PIL import Image
from io import BytesIO

def remove_ad_blocks(html_content):
    """네이버 블로그 광고 블록 제거"""
    print("\n🧹 광고 블록 제거 중...")

    # 광고 패턴 목록
    ad_patterns = [
        # 패턴 1: ad_power_content_wrap
        r'<div\s+class="ad_power_content_wrap"[^>]*>.*?</div>\s*</div>',
        # 패턴 2: ssp-adcontent
        r'<div\s+class="ssp-adcontent"[^>]*>.*?</div>',
        # 패턴 3: data-ad 속성
        r'<div\s+[^>]*data-ad="true"[^>]*>.*?</div>',
        # 패턴 4: se-component 광고
        r'<div\s+class="se-component[^"]*"\s+[^>]*data-ad[^>]*>.*?</div>',
    ]

    original_length = len(html_content)
    cleaned_html = html_content

    for pattern in ad_patterns:
        cleaned_html = re.sub(pattern, '', cleaned_html, flags=re.DOTALL | re.IGNORECASE)

    removed_size = original_length - len(cleaned_html)
    if removed_size > 0:
        print(f"✓ 광고 블록 제거 완료 (제거된 크기: {removed_size:,} bytes)")
    else:
        print("✓ 제거할 광고 블록 없음")

    return cleaned_html

def extract_image_urls(html_content):
    """HTML에서 네이버 이미지 URL 추출 (광고 제거 후, 순서 보존)"""
    # 1. 광고 블록 먼저 제거
    clean_html = remove_ad_blocks(html_content)

    # 2. HTML 순서대로 모든 img 태그 찾기
    # postfiles.pstatic.net을 포함한 모든 img 태그를 순서대로 추출
    img_pattern = r'<img[^>]+src="(https://postfiles\.pstatic\.net/[^"]+)"[^>]*>'

    unique_urls = []
    seen = set()

    # re.finditer를 사용하여 순서대로 처리
    for match in re.finditer(img_pattern, clean_html):
        url = match.group(1)

        # 중복 제거 (base URL 기준)
        base_url = url.split('?')[0]
        if base_url not in seen:
            seen.add(base_url)
            # 고해상도 이미지 URL 사용
            if '?type=' in url:
                unique_urls.append(url)
            else:
                unique_urls.append(base_url + '?type=w773')

    return unique_urls

def download_image(url, save_dir, post_slug, index):
    """이미지 다운로드 및 JPG로 변환"""
    try:
        # User-Agent 헤더 추가 (네이버 차단 방지)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Referer': 'https://blog.naver.com/'
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # 이미지를 메모리에서 열기
        img = Image.open(BytesIO(response.content))

        # RGBA(투명도 있음) 이미지를 RGB로 변환
        if img.mode in ('RGBA', 'LA', 'P'):
            # 흰색 배경 생성
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
            img = background
        elif img.mode != 'RGB':
            img = img.convert('RGB')

        # 파일명 생성: 항상 .jpg 확장자 사용
        filename = f"{post_slug}-{index:02d}.jpg"
        filepath = save_dir / filename

        # JPG로 저장 (품질 95)
        img.save(filepath, 'JPEG', quality=95, optimize=True)

        print(f"✓ 다운로드 완료: {filename}")
        return filename

    except Exception as e:
        print(f"✗ 다운로드 실패 ({url}): {e}")
        return None

def update_markdown(md_file, image_mapping):
    """마크다운 파일의 이미지 URL 업데이트"""
    if not os.path.exists(md_file):
        print(f"✗ 마크다운 파일을 찾을 수 없습니다: {md_file}")
        return

    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 네이버 이미지 URL을 로컬 경로로 변경
    for old_url, new_filename in image_mapping.items():
        base_url = old_url.split('?')[0]
        # 여러 패턴으로 매칭
        patterns = [
            old_url,
            base_url,
            base_url + r'\?type=w\d+',
        ]

        for pattern in patterns:
            content = re.sub(
                pattern,
                f'/images/posts/{new_filename}',
                content
            )

    # 파일 저장
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✓ 마크다운 파일 업데이트 완료: {md_file}")

def main():
    if len(sys.argv) < 3:
        print("사용법: python3 download_naver_images.py <HTML파일> <포스트슬러그>")
        print("예시: python3 download_naver_images.py naver.html kirimugiya-jinroku")
        sys.exit(1)

    html_file = sys.argv[1]
    post_slug = sys.argv[2]

    # HTML 파일 읽기
    if not os.path.exists(html_file):
        print(f"✗ 파일을 찾을 수 없습니다: {html_file}")
        sys.exit(1)

    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # 이미지 URL 추출 (광고 제거 포함)
    image_urls = extract_image_urls(html_content)

    print(f"\n" + "="*60)
    print(f"📊 이미지 추출 결과")
    print(f"="*60)
    print(f"✓ 광고 제거 후 발견된 콘텐츠 이미지: {len(image_urls)}개")
    print(f"✓ 다운로드할 이미지: {post_slug}-01.jpg ~ {post_slug}-{len(image_urls):02d}.jpg")
    print(f"="*60 + "\n")

    if not image_urls:
        print("✗ 이미지를 찾을 수 없습니다.")
        print("💡 힌트: HTML 파일에 <div class=\"se-component se-image\"> 구조가 있는지 확인하세요.")
        sys.exit(0)

    # 저장 디렉토리 생성
    save_dir = Path('static/images/posts')
    save_dir.mkdir(parents=True, exist_ok=True)

    # 이미지 다운로드
    # 특수 규칙: 첫 번째 이미지는 스킵, 두 번째 이미지를 01, 02로 중복 저장
    image_mapping = {}
    for i, url in enumerate(image_urls, 1):
        if i == 1:
            # 첫 번째 이미지는 스킵
            print(f"[{i}/{len(image_urls)}] 첫 번째 이미지 스킵 (광고 또는 불필요 이미지)")
            continue
        elif i == 2:
            # 두 번째 이미지를 01, 02로 2번 저장
            print(f"[{i}/{len(image_urls)}] 다운로드 중... (01, 02로 중복 저장)")
            filename1 = download_image(url, save_dir, post_slug, 1)
            filename2 = download_image(url, save_dir, post_slug, 2)
            if filename1 and filename2:
                image_mapping[url] = filename1  # 매핑은 01로
        else:
            # 세 번째 이미지부터는 원래 순서대로 (03, 04, 05...)
            print(f"[{i}/{len(image_urls)}] 다운로드 중...")
            filename = download_image(url, save_dir, post_slug, i)
            if filename:
                image_mapping[url] = filename

    print(f"\n" + "="*60)
    print(f"✅ 다운로드 완료!")
    print(f"="*60)
    print(f"✓ 성공: {len(image_mapping)}개 이미지")
    print(f"✓ 실패: {len(image_urls) - len(image_mapping)}개 이미지")
    print(f"✓ 저장 위치: static/images/posts/")
    print(f"="*60 + "\n")

    # 마크다운 파일 업데이트
    md_file = f"content/ko/posts/{post_slug}.md"
    if os.path.exists(md_file):
        update_markdown(md_file, image_mapping)
    else:
        print(f"ℹ️  마크다운 파일이 없습니다: {md_file}")
        print("📝 나중에 수동으로 이미지 경로를 업데이트해주세요:")
        for i, (old_url, new_filename) in enumerate(image_mapping.items(), 1):
            print(f"   {i}. /images/posts/{new_filename}")

    print("\n🎉 모든 작업 완료!")

if __name__ == '__main__':
    main()
