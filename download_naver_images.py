#!/usr/bin/env python3
"""
네이버 블로그 이미지 다운로드 스크립트

사용법:
    python3 download_naver_images.py <HTML파일경로> <포스트슬러그>

예시:
    python3 download_naver_images.py naver_blog.html kirimugiya-jinroku
"""

import re
import os
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse, unquote
from PIL import Image
from io import BytesIO

def extract_image_urls(html_content):
    """HTML에서 네이버 이미지 URL 추출"""
    # postfiles.pstatic.net 이미지 URL 패턴
    pattern = r'https://postfiles\.pstatic\.net/[^"\'?\s]+'
    urls = re.findall(pattern, html_content)

    # 중복 제거 및 type=w773 형식만 유지
    unique_urls = []
    seen = set()

    for url in urls:
        # ?type=w773 등의 파라미터 제거한 base URL
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

    # 이미지 URL 추출
    image_urls = extract_image_urls(html_content)
    print(f"\n총 {len(image_urls)}개의 이미지를 찾았습니다.\n")

    if not image_urls:
        print("✗ 이미지를 찾을 수 없습니다.")
        sys.exit(0)

    # 저장 디렉토리 생성
    save_dir = Path('static/images/posts')
    save_dir.mkdir(parents=True, exist_ok=True)

    # 이미지 다운로드
    image_mapping = {}
    for i, url in enumerate(image_urls, 1):
        print(f"[{i}/{len(image_urls)}] 다운로드 중...")
        filename = download_image(url, save_dir, post_slug, i)
        if filename:
            image_mapping[url] = filename

    print(f"\n✓ 총 {len(image_mapping)}개 이미지 다운로드 완료\n")

    # 마크다운 파일 업데이트
    md_file = f"content/ko/posts/{post_slug}.md"
    if os.path.exists(md_file):
        update_markdown(md_file, image_mapping)
    else:
        print(f"\n마크다운 파일이 없습니다: {md_file}")
        print("나중에 수동으로 이미지 경로를 업데이트해주세요:")
        for old_url, new_filename in image_mapping.items():
            print(f"  {old_url} → /images/posts/{new_filename}")

    print("\n✓ 완료!")

if __name__ == '__main__':
    main()
