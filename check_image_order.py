#!/usr/bin/env python3
"""
이미지 순서 검증 스크립트
네이버 HTML과 Hugo 마크다운의 이미지 순서가 일치하는지 확인합니다.
"""

import re
import sys
from pathlib import Path
from bs4 import BeautifulSoup


def extract_naver_images(html_content):
    """
    네이버 HTML에서 모든 이미지를 순서대로 추출
    - 단일 이미지 (se-image)
    - 이미지 그룹 (se-imageGroup)의 각 이미지
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    images = []

    # se-main-container 내의 모든 이미지 컴포넌트를 순서대로 찾기
    main_container = soup.find('div', class_='se-main-container')
    if not main_container:
        print("❌ Error: se-main-container not found in HTML")
        return []

    # 모든 이미지 컴포넌트를 순서대로 처리
    for component in main_container.find_all(['div'], class_=re.compile(r'se-component')):
        # 단일 이미지
        if 'se-image' in component.get('class', []):
            img = component.find('img', class_='se-image-resource')
            if img and img.get('src'):
                caption_elem = component.find('div', class_='se-caption')
                caption = caption_elem.get_text(strip=True) if caption_elem else "No caption"
                images.append({
                    'type': 'single',
                    'src': img['src'],
                    'caption': caption
                })

        # 이미지 그룹 (2개, 3개, 4개 등)
        elif 'se-imageGroup' in component.get('class', []):
            group_images = component.find_all('img', class_='se-image-resource')
            caption_elem = component.find('div', class_='se-caption')
            group_caption = caption_elem.get_text(strip=True) if caption_elem else "No caption"

            for idx, img in enumerate(group_images):
                if img.get('src'):
                    images.append({
                        'type': f'group ({len(group_images)} images)',
                        'src': img['src'],
                        'caption': f"{group_caption} [{idx+1}/{len(group_images)}]"
                    })

    return images


def extract_hugo_images(md_content, post_slug):
    """
    Hugo 마크다운에서 모든 이미지를 순서대로 추출
    - featured_image (Front Matter)
    - body images (<figure> 태그)
    """
    images = []

    # 1. featured_image 추출 (Front Matter)
    featured_match = re.search(r'featured_image:\s*"(/images/posts/[^"]+)"', md_content)
    if featured_match:
        featured_img = featured_match.group(1)
        images.append({
            'type': 'featured',
            'path': featured_img,
            'caption': 'Featured image (Front Matter)'
        })

    # 2. body images 추출 (<figure> 태그)
    figure_pattern = re.compile(
        r'<figure>\s*<img src="(/images/posts/[^"]+)"\s+alt="([^"]*)">.*?<figcaption>([^<]*)</figcaption>\s*</figure>',
        re.DOTALL
    )

    for match in figure_pattern.finditer(md_content):
        img_path = match.group(1)
        alt_text = match.group(2)
        caption = match.group(3)
        images.append({
            'type': 'body',
            'path': img_path,
            'alt': alt_text,
            'caption': caption
        })

    return images


def compare_images(naver_images, hugo_images, post_slug):
    """
    네이버와 Hugo 이미지를 비교하여 불일치 검출
    """
    print("\n" + "="*80)
    print(f"📊 이미지 순서 검증: {post_slug}")
    print("="*80)

    print(f"\n📌 네이버 HTML: {len(naver_images)}개 이미지")
    print(f"📌 Hugo 마크다운: {len(hugo_images)}개 이미지")

    # 첫 번째 이미지는 featured_image (커버)
    if len(hugo_images) == 0:
        print("\n❌ Hugo 이미지가 없습니다!")
        return False

    if hugo_images[0]['type'] != 'featured':
        print("\n⚠️  Warning: 첫 번째 이미지가 featured_image가 아닙니다!")

    # 네이버와 Hugo의 본문 이미지 비교
    # 네이버 이미지들은 모두 본문 이미지
    # Hugo는 featured (01.jpg) + body images (02.jpg~)
    naver_body_count = len(naver_images)
    hugo_body_count = len(hugo_images) - 1  # featured_image 제외

    print(f"\n📊 본문 이미지 비교:")
    print(f"   네이버: {naver_body_count}개")
    print(f"   Hugo:   {hugo_body_count}개")

    if naver_body_count != hugo_body_count:
        print(f"\n❌ 이미지 개수 불일치!")
        print(f"   차이: {abs(naver_body_count - hugo_body_count)}개")

        if hugo_body_count > naver_body_count:
            print(f"   ⚠️  Hugo에 {hugo_body_count - naver_body_count}개의 추가 이미지가 있습니다!")
            print(f"   네이버에 없는 이미지를 Hugo에서 삭제해야 합니다.")
        else:
            print(f"   ⚠️  Hugo에 {naver_body_count - hugo_body_count}개의 이미지가 부족합니다!")

        return False

    # 상세 비교
    print(f"\n📋 상세 이미지 매핑:")
    print("-" * 80)

    all_match = True
    for i in range(naver_body_count):
        naver_img = naver_images[i]
        hugo_img = hugo_images[i + 1]  # featured_image 건너뛰기

        expected_num = str(i + 2).zfill(2)  # 02, 03, 04...
        actual_num_match = re.search(r'-(\d+)\.jpg', hugo_img['path'])
        actual_num = actual_num_match.group(1) if actual_num_match else "??"

        match_status = "✅" if expected_num == actual_num else "❌"

        print(f"\n{match_status} 이미지 #{i+1}:")
        print(f"   네이버: {naver_img['caption'][:60]}")
        print(f"   Hugo:   {hugo_img['caption'][:60]}")
        print(f"   파일:   {post_slug}-{actual_num}.jpg (예상: {expected_num}.jpg)")

        if expected_num != actual_num:
            all_match = False

    print("\n" + "="*80)
    if all_match and naver_body_count == hugo_body_count:
        print("✅ 모든 이미지가 올바른 순서로 매핑되었습니다!")
        return True
    else:
        print("❌ 이미지 순서 불일치가 발견되었습니다!")
        return False


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 check_image_order.py <naver_html_file> <post_slug>")
        print("\nExample:")
        print("  python3 check_image_order.py naver.md japan-convenience-store-shopping-best-10")
        sys.exit(1)

    html_file = sys.argv[1]
    post_slug = sys.argv[2]

    # 파일 존재 확인
    if not Path(html_file).exists():
        print(f"❌ Error: HTML file not found: {html_file}")
        sys.exit(1)

    md_file_en = Path(f"content/en/posts/{post_slug}.md")
    if not md_file_en.exists():
        print(f"❌ Error: Hugo markdown file not found: {md_file_en}")
        sys.exit(1)

    # HTML 파일 읽기
    print(f"📖 Reading Naver HTML: {html_file}")
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Hugo 마크다운 읽기
    print(f"📖 Reading Hugo markdown: {md_file_en}")
    with open(md_file_en, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # 이미지 추출
    print("\n🔍 Extracting images from Naver HTML...")
    naver_images = extract_naver_images(html_content)

    print(f"🔍 Extracting images from Hugo markdown...")
    hugo_images = extract_hugo_images(md_content, post_slug)

    # 비교
    is_valid = compare_images(naver_images, hugo_images, post_slug)

    if not is_valid:
        print("\n💡 수정 방법:")
        print("   1. 네이버에 없는 이미지를 Hugo에서 삭제")
        print("   2. 이미지 번호를 올바르게 재배치")
        print("   3. 다시 검증 실행")
        sys.exit(1)
    else:
        print("\n🎉 검증 완료! 모든 이미지가 올바르게 매핑되었습니다.")
        sys.exit(0)


if __name__ == "__main__":
    main()
