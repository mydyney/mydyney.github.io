#!/usr/bin/env python3
"""
Convert English categories to Japanese in all Japanese blog posts
"""

import os
import re
from pathlib import Path

# English to Japanese category mapping
CATEGORY_MAPPING = {
    # Main categories
    "Disneyland": "ディズニーランド",
    "Festival Calendar": "イベントカレンダー",
    "Festival Guide": "フェスティバルガイド",
    "Restaurants": "レストラン",
    "Shinjuku/Shin-Okubo": "新宿・新大久保",
    "Transportation": "交通",
    "Travel Guide": "旅行ガイド",
    "Travel Info": "旅行情報",
    "Travel": "旅行",
    "Yokohama": "横浜",
    "Events": "イベント",
    "Events & Festivals": "イベント・フェスティバル",
    "Food & Dining": "グルメ",
    "Food Guide": "グルメガイド",
    "Shopping": "ショッピング",
    "Shopping & Guides": "ショッピング・ガイド",

    # Tokyo-specific
    "Tokyo Attractions": "東京観光スポット",
    "Tokyo Events": "東京イベント",
    "Tokyo Food": "東京グルメ",
    "Tokyo Shopping": "東京ショッピング",
    "Tokyo Sightseeing": "東京観光",
    "Tokyo Travel Guide": "東京旅行ガイド",
    "Tokyo Travel Info": "東京旅行情報",
    "Tokyo Itinerary": "東京旅行プラン",

    # Areas
    "Roppongi/Hiroo": "六本木・広尾",
    "Shibuya & Harajuku": "渋谷・原宿",
    "Meguro & Ebisu": "目黒・恵比寿",
    "Yokohama & Kamakura": "横浜・鎌倉",
    "Shimbashi/Shiodome": "新橋・汐留",
    "Shimbashi": "新橋",
    "Omotesando": "表参道",
    "Shinjuku": "新宿",
    "Ebisu": "恵比寿",
    "Narita Airport": "成田空港",

    # Specific topics
    "Restaurant Reviews": "レストランレビュー",
    "Autumn in Tokyo": "東京の秋",
    "Christmas": "クリスマス",
}

def convert_categories_in_file(filepath):
    """Convert English categories to Japanese in a single file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the categories line
    categories_match = re.search(r'^categories: \[(.*?)\]', content, re.MULTILINE)
    if not categories_match:
        print(f"No categories found in {filepath}")
        return False

    categories_str = categories_match.group(1)

    # Extract individual categories
    categories = [cat.strip().strip('"') for cat in categories_str.split(',')]

    # Convert English categories to Japanese
    converted_categories = []
    changed = False
    for cat in categories:
        if cat in CATEGORY_MAPPING:
            converted_categories.append(CATEGORY_MAPPING[cat])
            changed = True
        else:
            # Keep category as is if not in mapping (already Japanese or unknown)
            converted_categories.append(cat)

    if not changed:
        return False

    # Create new categories line
    new_categories_str = ', '.join(f'"{cat}"' for cat in converted_categories)
    new_categories_line = f'categories: [{new_categories_str}]'

    # Replace in content
    new_content = re.sub(
        r'^categories: \[.*?\]',
        new_categories_line,
        content,
        flags=re.MULTILINE
    )

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

def main():
    """Convert categories in all Japanese posts"""
    ja_posts_dir = Path('content/ja/posts')

    if not ja_posts_dir.exists():
        print(f"Directory {ja_posts_dir} does not exist!")
        return

    processed = 0
    for md_file in ja_posts_dir.glob('*.md'):
        if md_file.name == '_index.md':
            continue

        if convert_categories_in_file(md_file):
            print(f"✓ {md_file.name}")
            processed += 1

    print(f"\n✅ Converted categories in {processed} files")

if __name__ == '__main__':
    main()
