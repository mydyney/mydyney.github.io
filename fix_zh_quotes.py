#!/usr/bin/env python3
"""Fix malformed quotation marks in Chinese front matter."""

import os
import re
from pathlib import Path

def fix_quotes_in_file(filepath):
    """Fix malformed quotation marks in YAML front matter."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into front matter and body
    parts = content.split('---', 2)
    if len(parts) < 3:
        print(f"Skipping {filepath}: No front matter found")
        return False

    front_matter = parts[1]
    body = parts[2]

    # Fix the malformed pattern: 」value」 → "value"
    # This pattern appears in title, description, summary, translationKey, tags, categories, featured_image

    # Pattern 1: 」value」 at the start/end of a value → "value"
    fixed_fm = re.sub(r': 」([^」\n]+)」', r': "\1"', front_matter)

    # Pattern 2: For array values like [」tag1」, 」tag2」]
    fixed_fm = re.sub(r'」([^」\[\]\n,]+)」', r'"\1"', fixed_fm)

    if fixed_fm != front_matter:
        # Reconstruct the file
        new_content = '---' + fixed_fm + '---' + body
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True

    return False

def main():
    """Fix all Chinese posts."""
    zh_posts_dir = Path('content/zh-cn/posts')

    if not zh_posts_dir.exists():
        print(f"Directory {zh_posts_dir} not found")
        return

    fixed_count = 0
    total_count = 0

    for filepath in zh_posts_dir.glob('*.md'):
        total_count += 1
        if fix_quotes_in_file(filepath):
            fixed_count += 1
            print(f"✓ Fixed: {filepath.name}")
        else:
            print(f"  Skipped: {filepath.name}")

    print(f"\n{'='*60}")
    print(f"Total files processed: {total_count}")
    print(f"Files fixed: {fixed_count}")
    print(f"Files skipped: {total_count - fixed_count}")

if __name__ == '__main__':
    main()
