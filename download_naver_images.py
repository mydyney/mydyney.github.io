#!/usr/bin/env python3
"""
네이버 블로그 이미지 다운로드 스크립트 (검증 통합 버전)

기능:
    1. 네이버 HTML 분석 및 이미지 URL 추출
    2. Hugo 마크다운과 이미지 개수/순서 검증
    3. 검증 통과 시에만 이미지 다운로드
    4. JPG 형식으로 변환 및 최적화

사용법:
    python3 download_naver_images.py <HTML파일경로> <포스트슬러그>

예시:
    python3 download_naver_images.py naver_blog.html japan-convenience-store-shopping-best-10

출력:
    - static/images/posts/{slug}-01.jpg (featured image)
    - static/images/posts/{slug}-02.jpg (첫 번째 본문 이미지)
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
            if img and img.get('src'):
                caption_elem = component.find('div', class_='se-caption')
                caption = caption_elem.get_text(strip=True) if caption_elem else "No caption"

                # 고해상도 URL 사용
                url = img['src']
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
                if img.get('src'):
                    url = img['src']
                    if '?type=' not in url:
                        url = url.split('?')[0] + '?type=w773'

                    images.append({
                        'url': url,
                        'caption': f"{group_caption} [{idx+1}/{len(group_images)}]",
                        'type': f'group-{len(group_images)}'
                    })

    return images


def extract_hugo_images(md_content):
    """
    Hugo 마크다운에서 모든 이미지를 순서대로 추출
    - 단일 figure 태그와 image-group 내부의 figure 모두 감지

    Returns:
        list: [{'path': str, 'caption': str, 'type': str}, ...]
    """
    images = []

    # 1. featured_image 추출 (Front Matter)
    featured_match = re.search(r'featured_image:\s*"(/images/posts/[^"]+)"', md_content)
    if featured_match:
        images.append({
            'path': featured_match.group(1),
            'caption': 'Featured image',
            'type': 'featured'
        })

    # 2. body images 추출
    # 패턴: <figure> 내부의 <img> 태그를 모두 찾음 (단일 figure 또는 image-group 내부 모두 포함)
    # <figure>와 </figure> 사이에 있는 <img> 태그만 매칭
    figure_pattern = re.compile(
        r'<figure[^>]*>\s*<img src="(/images/posts/[^"]+)"\s+alt="([^"]*)"[^>]*>',
        re.DOTALL
    )

    for match in figure_pattern.finditer(md_content):
        images.append({
            'path': match.group(1),
            'alt': match.group(2),
            'caption': "Body image",
            'type': 'body'
        })

    return images


def validate_image_mapping(naver_images, hugo_images, post_slug):
    """
    네이버와 Hugo 이미지를 비교하여 검증

    Returns:
        bool: 검증 통과 여부
    """
    print("\n" + "="*80)
    print(f"🔍 이미지 순서 검증: {post_slug}")
    print("="*80)

    print(f"\n📊 이미지 개수:")
    print(f"   네이버 HTML: {len(naver_images)}개")
    print(f"   Hugo 마크다운: {len(hugo_images)}개")

    # Hugo의 첫 이미지는 featured_image여야 함
    if len(hugo_images) == 0:
        print("\n❌ Hugo 마크다운에 이미지가 없습니다!")
        return False

    if hugo_images[0]['type'] != 'featured':
        print("\n⚠️  Warning: 첫 번째 이미지가 featured_image가 아닙니다!")

    # 네이버 이미지 개수 = Hugo 이미지 개수 - 1 (featured 제외)
    naver_count = len(naver_images)
    hugo_body_count = len(hugo_images) - 1

    print(f"\n📊 본문 이미지 비교:")
    print(f"   네이버: {naver_count}개")
    print(f"   Hugo:   {hugo_body_count}개 (featured 제외)")

    if naver_count != hugo_body_count:
        print(f"\n❌ 이미지 개수 불일치!")
        print(f"   차이: {abs(naver_count - hugo_body_count)}개")

        if hugo_body_count > naver_count:
            print(f"\n⚠️  Hugo에 {hugo_body_count - naver_count}개의 추가 이미지가 있습니다!")
            print(f"   네이버에 없는 이미지를 Hugo에서 삭제해야 합니다.")
        else:
            print(f"\n⚠️  Hugo에 {naver_count - hugo_body_count}개의 이미지가 부족합니다!")
            print(f"   Hugo 마크다운에 이미지를 추가해야 합니다.")

        print("\n💡 수정 방법:")
        print("   1. Hugo 마크다운 파일을 열어 이미지 개수를 확인하세요")
        print("   2. 네이버 HTML과 동일한 개수로 맞추세요")
        print("   3. 다시 이 스크립트를 실행하세요")
        return False

    # 순서 검증
    print(f"\n📋 이미지 매핑 검증:")
    print("-" * 80)

    all_match = True
    for i in range(naver_count):
        naver_img = naver_images[i]
        hugo_img = hugo_images[i + 1]  # featured_image 건너뛰기

        expected_num = str(i + 2).zfill(2)  # 02, 03, 04...
        actual_num_match = re.search(r'-(\d+)\.jpg', hugo_img['path'])
        actual_num = actual_num_match.group(1) if actual_num_match else "??"

        match_status = "✅" if expected_num == actual_num else "❌"

        print(f"{match_status} 이미지 #{i+1}:")
        print(f"   네이버: {naver_img['caption'][:60]}")
        print(f"   Hugo:   {hugo_img['caption'][:60]}")
        print(f"   파일:   {post_slug}-{actual_num}.jpg (예상: {expected_num}.jpg)")

        if expected_num != actual_num:
            all_match = False

    print("\n" + "="*80)

    if all_match:
        print("✅ 검증 통과! 이미지 다운로드를 시작합니다.")
        return True
    else:
        print("❌ 검증 실패! 이미지 순서를 수정한 후 다시 시도하세요.")
        print("\n💡 수정 방법:")
        print("   1. Hugo 마크다운에서 이미지 번호가 순차적인지 확인")
        print("   2. 02, 03, 04, 05... (누락 없이)")
        print("   3. 네이버에 없는 이미지를 Hugo에서 삭제")
        return False


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
    if len(sys.argv) < 3:
        print("사용법: python3 download_naver_images.py <HTML파일> <포스트슬러그>")
        print("예시: python3 download_naver_images.py naver.html japan-convenience-store-shopping-best-10")
        sys.exit(1)

    html_file = sys.argv[1]
    post_slug = sys.argv[2]

    # 1. HTML 파일 확인
    if not os.path.exists(html_file):
        print(f"❌ HTML 파일을 찾을 수 없습니다: {html_file}")
        sys.exit(1)

    # 2. Hugo 마크다운 파일 확인
    md_file_en = Path(f"content/en/posts/{post_slug}.md")
    md_file_ja = Path(f"content/ja/posts/{post_slug}.md")

    md_file = None
    if md_file_en.exists():
        md_file = md_file_en
    elif md_file_ja.exists():
        md_file = md_file_ja
    else:
        print(f"❌ Hugo 마크다운 파일을 찾을 수 없습니다:")
        print(f"   - {md_file_en}")
        print(f"   - {md_file_ja}")
        print("\n💡 먼저 Hugo 마크다운 파일을 작성한 후 이미지를 다운로드하세요.")
        sys.exit(1)

    print(f"📖 읽기: {html_file}")
    print(f"📖 읽기: {md_file}")

    # 3. 네이버 HTML에서 이미지 추출
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    print("\n🔍 네이버 HTML 분석 중...")
    naver_images = extract_naver_images(html_content)

    if not naver_images:
        print("❌ 네이버 HTML에서 이미지를 찾을 수 없습니다.")
        sys.exit(1)

    print(f"✓ 발견된 이미지: {len(naver_images)}개")
    for i, img in enumerate(naver_images[:3], 1):
        print(f"   {i}. {img['caption'][:50]}...")
    if len(naver_images) > 3:
        print(f"   ... 외 {len(naver_images) - 3}개")

    # 4. Hugo 마크다운에서 이미지 추출
    print("\n🔍 Hugo 마크다운 분석 중...")
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    hugo_images = extract_hugo_images(md_content)

    if not hugo_images:
        print("❌ Hugo 마크다운에 이미지가 없습니다.")
        print("\n💡 먼저 Hugo 마크다운에 <figure> 태그로 이미지를 추가하세요.")
        sys.exit(1)

    print(f"✓ 발견된 이미지: {len(hugo_images)}개")

    # 5. 검증
    is_valid = validate_image_mapping(naver_images, hugo_images, post_slug)

    if not is_valid:
        print("\n" + "="*80)
        print("🛑 검증 실패로 다운로드를 중단합니다.")
        print("="*80)
        sys.exit(1)

    # 6. 다운로드 시작
    print("\n" + "="*80)
    print("💾 이미지 다운로드 시작")
    print("="*80)

    save_dir = Path('static/images/posts')
    save_dir.mkdir(parents=True, exist_ok=True)

    # 첫 번째 이미지: featured_image (01.jpg)
    print(f"\n[1/{len(naver_images)}] featured_image (01.jpg):")
    download_image(naver_images[0]['url'], save_dir, post_slug, 1)

    # 나머지 이미지: body images (02.jpg~)
    success_count = 1
    for i, img in enumerate(naver_images, 1):
        if i == 1:
            continue  # 이미 다운로드함

        print(f"\n[{i}/{len(naver_images)}] body image ({i+1:02d}.jpg):")
        filename = download_image(img['url'], save_dir, post_slug, i + 1)
        if filename:
            success_count += 1

    # 7. 완료
    print("\n" + "="*80)
    print("✅ 다운로드 완료!")
    print("="*80)
    print(f"✓ 성공: {success_count}/{len(naver_images)}개 이미지")
    print(f"✓ 저장 위치: static/images/posts/")
    print(f"✓ 파일 형식: {post_slug}-01.jpg ~ {post_slug}-{len(naver_images)+1:02d}.jpg")
    print("="*80)

    print("\n🎉 모든 작업 완료!")
    print("\n📝 다음 단계:")
    print("   1. static/images/posts/ 디렉토리에서 다운로드된 이미지 확인")
    print("   2. Hugo 로컬 서버로 미리보기: hugo server -D")
    print("   3. 문제없으면 commit & push")


if __name__ == '__main__':
    main()
