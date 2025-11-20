#!/usr/bin/env python3
"""
Fix unmapped Naver blog links to TODO format with href="#"
"""

import re
import os
import glob

def fix_naver_links_in_file(filepath):
    """Convert Naver blog links to TODO format"""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match Naver blog links in <a> tags
    # Matches: <a href="https://blog.naver.com/tokyomate/NUMBER" ...>LINK_TEXT</a>
    pattern = r'<a\s+href="https://blog\.naver\.com/tokyomate/(\d+)"([^>]*)>(.*?)</a>'

    def replace_link(match):
        naver_id = match.group(1)
        attrs = match.group(2)  # Other attributes like target="_blank"
        link_text = match.group(3)

        # Determine if it's Japanese or English based on file path
        is_japanese = '/ja/posts/' in filepath
        slug_placeholder = '/ja/posts/[SLUG_TBD]/' if is_japanese else '/posts/[SLUG_TBD]/'

        # Create TODO comment and new link
        todo_comment = f'''<!-- TODO: Update link after migration
     Naver: https://blog.naver.com/tokyomate/{naver_id}
     Hugo: {slug_placeholder} -->
<a href="#" style="color: #667eea;">{link_text}</a>'''

        return todo_comment

    # Replace all Naver links
    new_content = re.sub(pattern, replace_link, content)

    # Count replacements
    original_count = len(re.findall(pattern, content))

    if original_count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return original_count

    return 0

def main():
    # Find all markdown files in content/en/posts and content/ja/posts
    en_posts = glob.glob('/home/user/mydyney.github.io/content/en/posts/*.md')
    ja_posts = glob.glob('/home/user/mydyney.github.io/content/ja/posts/*.md')

    all_posts = en_posts + ja_posts

    total_fixed = 0
    files_modified = 0

    for filepath in all_posts:
        count = fix_naver_links_in_file(filepath)
        if count > 0:
            filename = os.path.basename(filepath)
            lang = 'JA' if '/ja/posts/' in filepath else 'EN'
            print(f"  ✅ {lang}: {filename} - Fixed {count} links")
            total_fixed += count
            files_modified += 1

    print(f"\n{'='*50}")
    print(f"Total: {total_fixed} Naver links converted to TODO format")
    print(f"Files modified: {files_modified}")
    print(f"{'='*50}")

if __name__ == '__main__':
    main()
