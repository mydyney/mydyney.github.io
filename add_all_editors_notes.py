#!/usr/bin/env python3
"""
Add Editor's Note to ALL remaining blog posts with language-specific content and correct Naver blog URL.
Reads LINK_MAPPING.md to get Naver IDs for each slug.
"""

import re
import os
from pathlib import Path

# Editor's Note templates by language
EDITORS_NOTE = {
    "en": '''
<div class="editors-note">
  <p style="text-align: left; font-style: italic;"><strong>Editor's Note</strong></p>
  <p style="background-color: #f7f7f7; padding: 15px; border-left: 4px solid #667eea; margin: 10px 0;">
    This article is based on the author's actual experiences and original content from <a href="https://blog.naver.com/tokyomate/{naver_id}" target="_blank" style="color: #667eea; text-decoration: underline;">blog.naver.com/tokyomate</a>. It has been translated and adapted to provide authentic travel information about Tokyo for global readers.
  </p>
</div>
''',
    "ja": '''
<div class="editors-note">
  <p style="text-align: left; font-style: italic;"><strong>編集者注</strong></p>
  <p style="background-color: #f7f7f7; padding: 15px; border-left: 4px solid #667eea; margin: 10px 0;">
    本記事は、筆者の実際の体験に基づき、公式ブログ <a href="https://blog.naver.com/tokyomate/{naver_id}" target="_blank" style="color: #667eea; text-decoration: underline;">blog.naver.com/tokyomate</a> に掲載されたオリジナルコンテンツを翻訳・再構成したものです。リアルな東京の旅情報をお届けします。
  </p>
</div>
''',
    "zh-cn": '''
<div class="editors-note">
  <p style="text-align: left; font-style: italic;"><strong>编者按</strong></p>
  <p style="background-color: #f7f7f7; padding: 15px; border-left: 4px solid #667eea; margin: 10px 0;">
    本文基于作者的亲身经历，编译自韩国原创博客 <a href="https://blog.naver.com/tokyomate/{naver_id}" target="_blank" style="color: #667eea; text-decoration: underline;">blog.naver.com/tokyomate</a>。内容经过翻译与调整，旨在为您分享真实可靠的东京旅行资讯。
  </p>
</div>
''',
}

def load_naver_mapping():
    """Load Naver ID to slug mapping from LINK_MAPPING.md."""
    mapping = {}

    try:
        with open('LINK_MAPPING.md', 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract mappings from the Quick Reference Table
        # Format: | 224024819592 | asakusa-complete-guide | 2025-09-28 | ✅ |
        pattern = r'\|\s*(\d+)\s*\|\s*([a-z0-9-]+)\s*\|.*?\|\s*✅\s*\|'
        matches = re.findall(pattern, content, re.MULTILINE)

        for naver_id, slug in matches:
            mapping[slug] = naver_id

        print(f"✅ Loaded {len(mapping)} mappings from LINK_MAPPING.md")
        return mapping

    except Exception as e:
        print(f"❌ Error loading LINK_MAPPING.md: {e}")
        return {}

def get_all_posts_without_note():
    """Get list of all post slugs that don't have Editor's Note yet."""
    posts_without_note = []

    # Check EN posts
    en_posts_dir = Path("content/en/posts")
    for post_file in en_posts_dir.glob("*.md"):
        try:
            with open(post_file, 'r', encoding='utf-8') as f:
                content = f.read()

            if 'editors-note' not in content:
                slug = post_file.stem
                posts_without_note.append(slug)

        except Exception as e:
            print(f"⚠️  Error reading {post_file}: {e}")

    return sorted(posts_without_note)

def add_editors_note(file_path, naver_id, lang):
    """Add Editor's Note to a blog post file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if Editor's Note already exists
        if 'editors-note' in content:
            return 'skipped'

        # Get the Editor's Note template for this language
        note_template = EDITORS_NOTE[lang].format(naver_id=naver_id)

        # Find the last </div> tag (closing blog-container)
        # Add Editor's Note before it
        if '</div>' not in content:
            return 'no_div'

        # Replace the last </div> with Editor's Note + </div>
        parts = content.rsplit('</div>', 1)
        if len(parts) != 2:
            return 'unexpected'

        new_content = parts[0] + note_template + '\n</div>' + parts[1]

        # Write the updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return 'success'

    except FileNotFoundError:
        return 'not_found'
    except Exception as e:
        return f'error: {e}'

def main():
    """Process all posts."""
    print("=" * 70)
    print("🚀 Adding Editor's Note to ALL remaining blog posts")
    print("=" * 70)
    print()

    # Load Naver ID mapping
    naver_mapping = load_naver_mapping()
    if not naver_mapping:
        print("❌ Failed to load Naver mapping. Aborting.")
        return

    # Get all posts without Editor's Note
    posts_to_process = get_all_posts_without_note()
    print(f"📊 Found {len(posts_to_process)} posts without Editor's Note")
    print()

    # Statistics
    stats = {
        'success': 0,
        'skipped': 0,
        'no_naver_id': 0,
        'errors': 0,
        'not_found': 0
    }

    # Process each post
    for i, slug in enumerate(posts_to_process, 1):
        print(f"[{i}/{len(posts_to_process)}] Processing: {slug}")

        # Get Naver ID for this slug
        if slug not in naver_mapping:
            print(f"  ⚠️  No Naver ID found in LINK_MAPPING.md")
            stats['no_naver_id'] += 1
            print()
            continue

        naver_id = naver_mapping[slug]
        print(f"  Naver ID: {naver_id}")

        # Process each language
        for lang in ['en', 'ja', 'zh-cn']:
            file_path = f"content/{lang}/posts/{slug}.md"
            result = add_editors_note(file_path, naver_id, lang)

            if result == 'success':
                print(f"  ✅ {lang.upper()}: Added Editor's Note")
                stats['success'] += 1
            elif result == 'skipped':
                print(f"  ⏭️  {lang.upper()}: Already has Editor's Note")
                stats['skipped'] += 1
            elif result == 'not_found':
                print(f"  ⚠️  {lang.upper()}: File not found")
                stats['not_found'] += 1
            else:
                print(f"  ❌ {lang.upper()}: {result}")
                stats['errors'] += 1

        print()

    # Final summary
    print("=" * 70)
    print("📊 FINAL SUMMARY")
    print("=" * 70)
    print(f"Posts processed: {len(posts_to_process)}")
    print(f"Successfully updated: {stats['success']}")
    print(f"Skipped (already had note): {stats['skipped']}")
    print(f"Missing Naver ID: {stats['no_naver_id']}")
    print(f"File not found: {stats['not_found']}")
    print(f"Errors: {stats['errors']}")
    print("=" * 70)

    # Calculate total files updated
    total_files = stats['success']
    print(f"\n✅ Total files updated: {total_files}")

    if stats['no_naver_id'] > 0:
        print(f"\n⚠️  {stats['no_naver_id']} posts are missing Naver IDs in LINK_MAPPING.md")

if __name__ == "__main__":
    main()
