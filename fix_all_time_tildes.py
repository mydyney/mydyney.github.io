#!/usr/bin/env python3
"""Fix tilde strikethrough issue in all blog posts with time ranges"""

import re
from pathlib import Path

def fix_time_tilde_issue(filepath):
    """Wrap time content with tildes in span tags to prevent Markdown processing"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Pattern 1: List items with time and tildes
    # - <strong>時間：</strong> 17:30~20:00
    # - <strong>Hours:</strong> 17:30~20:00
    pattern1 = r'(- <strong>(?:時間|時刻|Hours?|Time|营业时间)：?</strong> )([^<\n]+~[^<\n]+)'
    content = re.sub(pattern1, r'\1<span>\2</span>', content)
    
    # Pattern 2: Table cells with time and tildes
    # <td>17:30~20:00</td>
    pattern2 = r'(<td[^>]*>)(\d+:\d+~\d+:\d+)(</td>)'
    content = re.sub(pattern2, r'\1<span>\2</span>\3', content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    """Process all blog posts"""
    
    content_dirs = ['content/en/posts', 'content/ja/posts', 'content/zh-cn/posts']
    
    fixed_count = 0
    stats = {'en': 0, 'ja': 0, 'zh-cn': 0}
    
    for content_dir in content_dirs:
        lang = 'en' if '/en/' in content_dir else ('ja' if '/ja/' in content_dir else 'zh-cn')
        
        md_files = list(Path(content_dir).glob('*.md'))
        
        for filepath in md_files:
            if fix_time_tilde_issue(filepath):
                fixed_count += 1
                stats[lang] += 1
                print(f"✓ Fixed: {filepath.name} ({lang.upper()})")
    
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Total files fixed: {fixed_count}")
    print(f"  EN: {stats['en']} files")
    print(f"  JA: {stats['ja']} files")
    print(f"  ZH-CN: {stats['zh-cn']} files")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
