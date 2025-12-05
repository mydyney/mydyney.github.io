#!/usr/bin/env python3
"""
Convert English tags to Japanese in all Japanese blog posts
"""

import os
import re
from pathlib import Path

# English to Japanese tag mapping
TAG_MAPPING = {
    "andaz-hotel": "アンダーズホテル",
    "anime-merchandise": "アニメグッズ",
    "azabudai-hills": "麻布台ヒルズ",
    "azabujuban": "麻布十番",
    "bean to bar": "bean to bar",  # Keep as is (technical term)
    "business-district": "ビジネス街",
    "cash-only": "現金のみ",
    "cosplay": "コスプレ",
    "disneyland": "ディズニーランド",
    "family-events": "家族イベント",
    "gacha": "ガチャ",
    "gashapon": "ガシャポン",
    "halloween": "ハロウィン",
    "ikebukuro": "池袋",
    "izakaya": "居酒屋",
    "kabukicho": "歌舞伎町",
    "michelin": "ミシュラン",
    "observation-deck": "展望台",
    "pasmo": "パスモ",
    "shibuya": "渋谷",
    "shinjuku": "新宿",
    "sky-room-cafe": "スカイルームカフェ",
    "solamachi": "ソラマチ",
    "suica": "スイカ",
    "sweets": "スイーツ",
    "t-market": "Tマーケット",
    "taiyaki": "たい焼き",
    "teamlab-borderless": "チームラボボーダレス",
    "ticket-discount": "チケット割引",
    "tokyo": "東京",
    "tokyo-attractions": "東京観光",
    "tokyo-festivals": "東京祭り",
    "tokyo-guide": "東京ガイド",
    "tokyo-node": "東京ノード",
    "tokyo-observatory": "東京展望台",
    "tokyo-restaurants": "東京レストラン",
    "tokyo-shopping": "東京ショッピング",
    "tokyo-skytree": "東京スカイツリー",
    "tokyo-tower-view": "東京タワービュー",
    "toranomon-hills": "虎ノ門ヒルズ",
    "traditional-food": "和食",
    "transportation": "交通",
    "travel-tips": "旅行情報",
    "txt": "TXT",
    "2025": "2025",  # Keep numbers as is
}

def convert_tags_in_file(filepath):
    """Convert English tags to Japanese in a single file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the tags line
    tags_match = re.search(r'^tags: \[(.*?)\]', content, re.MULTILINE)
    if not tags_match:
        print(f"No tags found in {filepath}")
        return False

    tags_str = tags_match.group(1)

    # Extract individual tags
    tags = [tag.strip().strip('"') for tag in tags_str.split(',')]

    # Convert English tags to Japanese
    converted_tags = []
    for tag in tags:
        if tag in TAG_MAPPING:
            converted_tags.append(TAG_MAPPING[tag])
        else:
            # Keep tag as is if not in mapping (already Japanese or unknown)
            converted_tags.append(tag)

    # Create new tags line
    new_tags_str = ', '.join(f'"{tag}"' for tag in converted_tags)
    new_tags_line = f'tags: [{new_tags_str}]'

    # Replace in content
    new_content = re.sub(
        r'^tags: \[.*?\]',
        new_tags_line,
        content,
        flags=re.MULTILINE
    )

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

def main():
    """Convert tags in all Japanese posts"""
    ja_posts_dir = Path('content/ja/posts')

    if not ja_posts_dir.exists():
        print(f"Directory {ja_posts_dir} does not exist!")
        return

    processed = 0
    for md_file in ja_posts_dir.glob('*.md'):
        if md_file.name == '_index.md':
            continue

        print(f"Processing: {md_file.name}")
        if convert_tags_in_file(md_file):
            processed += 1

    print(f"\n✅ Converted tags in {processed} files")

if __name__ == '__main__':
    main()
