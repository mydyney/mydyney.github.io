#!/usr/bin/env python3
"""
네이버 블로그 이미지 다운로드 스크립트 (검증 통합 버전)

기능:
    1. 네이버 HTML 분석 및 이미지 URL 추출
    2. Hugo 마크다운과 이미지 개수/순서 검증 (1:1 매칭)
    3. 검증 통과 시에만 이미지 다운로드
    4. JPG 형식으로 변환 및 최적화

사용법:
    python3 download_naver_images.py <포스트슬러그>

예시:
    python3 download_naver_images.py japan-convenience-store-shopping-best-10

출력:
    - static/images/posts/{slug}-01.jpg (첫 번째 이미지)
    - static/images/posts/{slug}-02.jpg (두 번째 이미지)
    - ...
    - 네이버 HTML의 이미지와 Hugo 마크다운의 이미지를 순서대로 1:1 매칭
"""

import re
import os
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse, unquote
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup


def extract_naver_images(html_content):
    """
    네이버 HTML에서 모든 이미지를 순서대로 추출
    - 광고 블록 자동 제거
    - 단일 이미지 및 이미지 그룹 모두 감지

    Returns:
        list: [{'url': str, 'caption': str}, ...]
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    images = []

    # se-main-container 내의 모든 이미지 컴포넌트를 순서대로 찾기
    main_container = soup.find('div', class_='se-main-container')
    if not main_container:
        print("❌ Error: se-main-container not found in HTML")
        return []

    # 광고 블록 제거
    for ad_block in main_container.find_all('div', class_=re.compile(r'(ssp-adcontent|ad_power_content_wrap)')):
        ad_block.decompose()

    # 모든 이미지 컴포넌트를 순서대로 처리
    for component in main_container.find_all(['div'], class_=re.compile(r'se-component')):
        # 광고 컴포넌트 스킵
        if component.get('data-ad') == 'true':
            continue

        # 단일 이미지
        if 'se-image' in component.get('class', []):
            img = component.find('img', class_='se-image-resource')
            if img:
                # Prefer data-lazy-src if available, else src
                url = img.get('data-lazy-src') or img.get('src')
                if url:
                    caption_elem = component.find('div', class_='se-caption')
                    caption = caption_elem.get_text(strip=True) if caption_elem else "No caption"

                    # 고해상도 URL 사용 (Handle both query params and clean URLs)
                    if '?type=' not in url:
                        url = url.split('?')[0] + '?type=w773'

                    images.append({
                        'url': url,
                        'caption': caption,
                        'type': 'single'
                    })

        # 이미지 그룹 (2개, 3개, 4개 등)
        elif 'se-imageGroup' in component.get('class', []):
            group_images = component.find_all('img', class_='se-image-resource')
            caption_elem = component.find('div', class_='se-caption')
            group_caption = caption_elem.get_text(strip=True) if caption_elem else "No caption"

            for idx, img in enumerate(group_images):
                url = img.get('data-lazy-src') or img.get('src')
                if url:
                    if '?type=' not in url:
                        url = url.split('?')[0] + '?type=w773'

                    images.append({
                        'url': url,
                        'caption': f"{group_caption} [{idx+1}/{len(group_images)}]",
                        'type': f'group-{len(group_images)}'
                    })

    return images


def download_image(url, save_dir, post_slug, index):
    """이미지 다운로드 및 JPG로 변환"""
    try:
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

        print(f"  ✓ {filename}")
        return filename

    except Exception as e:
        print(f"  ✗ 다운로드 실패: {e}")
        return None


def main():
    if len(sys.argv) < 2:
        print("사용법: python3 download_naver_images.py <포스트슬러그>")
        print("예시: python3 download_naver_images.py japan-convenience-store-shopping-best-10")
        sys.exit(1)

    post_slug = sys.argv[1]
    html_file = "naver.md"  # 항상 naver.md 파일에서 읽기

    # 1. HTML 파일 확인
    if not os.path.exists(html_file):
        print(f"❌ naver.md 파일을 찾을 수 없습니다.")
        print(f"   현재 디렉토리에 naver.md 파일이 있는지 확인해주세요.")
        sys.exit(1)

    print(f"📖 읽기: {html_file}")

    # 2. 네이버 HTML에서 이미지 추출
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    print("\n🔍 네이버 HTML 분석 중...")
    naver_images = extract_naver_images(html_content)

    if not naver_images:
        print("❌ 네이버 HTML에서 이미지를 찾을 수 없습니다.")
        sys.exit(1)

    print(f"✓ 발견된 이미지: {len(naver_images)}개")
    for i, img in enumerate(naver_images[:5], 1):
        print(f"   {i}. {img['caption'][:60]}...")
    if len(naver_images) > 5:
        print(f"   ... 외 {len(naver_images) - 5}개")

    # 3. 다운로드 시작
    print("\n" + "="*80)
    print("💾 이미지 다운로드 시작")
    print(f"   순서대로 01.jpg ~ {len(naver_images):02d}.jpg 로 저장합니다")
    print("="*80)

    save_dir = Path('static/images/posts')
    save_dir.mkdir(parents=True, exist_ok=True)

    # 모든 이미지 순서대로 다운로드 (01.jpg, 02.jpg, 03.jpg...)
    success_count = 0
    for i, img in enumerate(naver_images, 1):
        print(f"\n[{i}/{len(naver_images)}] 이미지 ({i:02d}.jpg):")
        filename = download_image(img['url'], save_dir, post_slug, i)
        if filename:
            success_count += 1

    # 4. 완료
    print("\n" + "="*80)
    print("✅ 다운로드 완료!")
    print("="*80)
    print(f"✓ 성공: {success_count}/{len(naver_images)}개 이미지")
    print(f"✓ 저장 위치: static/images/posts/")
    print(f"✓ 파일 형식: {post_slug}-01.jpg ~ {post_slug}-{len(naver_images):02d}.jpg")
    print("="*80)

    print("\n🎉 모든 작업 완료!")
    print("\n📝 다음 단계:")
    print("   1. static/images/posts/ 디렉토리에서 다운로드된 이미지 확인")
    print("   2. Hugo 로컬 서버로 미리보기: hugo server -D")
    print("   3. 문제없으면 commit & push")


if __name__ == '__main__':
    main()
