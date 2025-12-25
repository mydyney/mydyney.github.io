#!/usr/bin/env python3
"""Add Editor's Note to the final 10 posts"""

import sys

# All 10 posts with their Naver IDs
POSTS = [
    ("hibiya-park-tokyo-guide", "224093593124"),
    ("jiyugaoka-tokyo-travel-guide", "224092707353"),
    ("miyashita-park-illumination-2024", "223689247336"),
    ("nihonbashi-tokyo-guide", "224042267263"),
    ("omotesando-guide-2025", "224027835049"),
    ("shibuya-station-coin-locker-luggage-storage-guide", "224107954391"),
    ("shimokitazawa-tokyo-travel-guide", "224096203397"),
    ("shinjuku-gashapon-shops-best-7", "224090178080"),
    ("shinjuku-neon-walk-tokyo-illumination-2025-2026", "224095124866"),
    ("tokyo-station-guide", "224031611221"),
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

def add_editors_note_to_file(file_path, naver_id, lang):
    """Add Editor's Note to a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if already has Editor's Note
        if 'editors-note' in content:
            return 'skipped'

        # Get template
        note = EDITORS_NOTE[lang].format(naver_id=naver_id)

        # Try to find closing </div> tag
        if '</div>' in content:
            parts = content.rsplit('</div>', 1)
            new_content = parts[0] + note + '\n</div>' + parts[1]
        else:
            # No closing div, just append to end
            new_content = content.rstrip() + '\n' + note

        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return 'success'

    except FileNotFoundError:
        return 'not_found'
    except Exception as e:
        return f'error: {e}'

def main():
    print("=" * 70)
    print("🚀 Adding Editor's Note to final 10 posts")
    print("=" * 70)
    print()

    success = 0
    skipped = 0
    not_found = 0
    errors = 0

    for i, (slug, naver_id) in enumerate(POSTS, 1):
        print(f"[{i}/10] {slug} (Naver: {naver_id})")

        for lang in ['en', 'ja', 'zh-cn']:
            file_path = f"content/{lang}/posts/{slug}.md"
            result = add_editors_note_to_file(file_path, naver_id, lang)

            if result == 'success':
                print(f"  ✅ {lang.upper()}: Added Editor's Note")
                success += 1
            elif result == 'skipped':
                print(f"  ⏭️  {lang.upper()}: Already has Editor's Note")
                skipped += 1
            elif result == 'not_found':
                print(f"  ⚠️  {lang.upper()}: File not found")
                not_found += 1
            else:
                print(f"  ❌ {lang.upper()}: {result}")
                errors += 1

        print()

    print("=" * 70)
    print("📊 SUMMARY")
    print("=" * 70)
    print(f"Successfully added: {success}")
    print(f"Skipped (already had): {skipped}")
    print(f"Files not found: {not_found}")
    print(f"Errors: {errors}")
    print("=" * 70)

if __name__ == "__main__":
    main()
