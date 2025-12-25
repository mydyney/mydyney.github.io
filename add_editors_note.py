#!/usr/bin/env python3
"""
Add Editor's Note to blog posts with language-specific content and correct Naver blog URL.
"""

import re
import sys

# List of posts to process: (slug, naver_id)
POSTS = [
    ("roppongi-attractions-guide", "223988228389"),
    ("shinanoya-roppongi-hills-supermarket", "223664743235"),
    ("ginza-guide-2025", "223989943826"),
    ("tokyo-september-festivals-2025", "223992588094"),
    ("don-quijote-shopping-guide-2025", "224022065518"),
    ("asakusa-complete-guide", "224024819592"),
    ("tokyo-october-festivals-2025", "224026292057"),
    ("harajuku-complete-guide-2025", "224030294691"),
    ("shibuya-complete-guide-2025", "224031114514"),
]

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

def add_editors_note(file_path, naver_id):
    """Add Editor's Note to a blog post file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if Editor's Note already exists
        if 'editors-note' in content:
            print(f"  ⏭️  Editor's Note already exists in {file_path}")
            return False

        # Determine language from file path
        if '/en/posts/' in file_path:
            lang = 'en'
        elif '/ja/posts/' in file_path:
            lang = 'ja'
        elif '/zh-cn/posts/' in file_path:
            lang = 'zh-cn'
        else:
            print(f"  ❌ Unknown language for {file_path}")
            return False

        # Get the Editor's Note template for this language
        note_template = EDITORS_NOTE[lang].format(naver_id=naver_id)

        # Find the last </div> tag (closing blog-container)
        # Add Editor's Note before it
        if '</div>' not in content:
            print(f"  ❌ No closing </div> tag found in {file_path}")
            return False

        # Replace the last </div> with Editor's Note + </div>
        parts = content.rsplit('</div>', 1)
        if len(parts) != 2:
            print(f"  ❌ Unexpected file structure in {file_path}")
            return False

        new_content = parts[0] + note_template + '\n</div>' + parts[1]

        # Write the updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"  ✅ Added Editor's Note to {file_path}")
        return True

    except FileNotFoundError:
        print(f"  ⚠️  File not found: {file_path}")
        return False
    except Exception as e:
        print(f"  ❌ Error processing {file_path}: {e}")
        return False

def main():
    """Process all posts."""
    print("🔄 Adding Editor's Note to blog posts...\n")

    total = 0
    successful = 0
    skipped = 0
    errors = 0

    for slug, naver_id in POSTS:
        print(f"📝 Processing: {slug} (Naver ID: {naver_id})")

        for lang in ['en', 'ja', 'zh-cn']:
            total += 1
            file_path = f"content/{lang}/posts/{slug}.md"

            result = add_editors_note(file_path, naver_id)

            if result is True:
                successful += 1
            elif result is False and 'already exists' in str(result):
                skipped += 1
            else:
                errors += 1

        print()

    print("=" * 60)
    print(f"📊 Summary:")
    print(f"  Total files processed: {total}")
    print(f"  Successfully updated: {successful}")
    print(f"  Skipped (already had note): {skipped}")
    print(f"  Errors: {errors}")
    print("=" * 60)

if __name__ == "__main__":
    main()
