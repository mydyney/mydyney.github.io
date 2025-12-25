#!/usr/bin/env python3
"""Fix tilde strikethrough issue in ALL blog posts"""

import re
from pathlib import Path

def fix_tilde_in_times(filepath):
    """Fix time ranges with tildes by wrapping in span tags"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = []
    
    # Pattern 1: List items with time containing ~
    # Matches: - <strong>Hours:</strong> 17:30~20:00
    pattern1 = r'(- <strong>(?:時間|时间|Hours?|Time|Horaires?|Tiempo|Ora|Tijd)：?\s*</strong>\s*)([^\n<]+\d+:\d+~[^\n<]+?)(\n)'
    
    def wrap_in_span(match):
        prefix = match.group(1)
        time_text = match.group(2).strip()
        suffix = match.group(3)
        
        # Skip if already wrapped
        if '<span>' in prefix or '<span>' in time_text:
            return match.group(0)
        
        changes.append(f"  • {time_text}")
        return f'{prefix}<span>{time_text}</span>{suffix}'
    
    content = re.sub(pattern1, wrap_in_span, content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, changes
    return False, []

def main():
    """Process all blog posts"""
    
    content_dirs = ['content/en/posts', 'content/ja/posts', 'content/zh-cn/posts']
    
    total_fixed = 0
    stats = {'en': 0, 'ja': 0, 'zh-cn': 0}
    
    print("Scanning all blog posts for tilde strikethrough issues...\n")
    
    for content_dir in content_dirs:
        lang = 'en' if '/en/' in content_dir else ('ja' if '/ja/' in content_dir else 'zh-cn')
        
        md_files = sorted(Path(content_dir).glob('*.md'))
        
        for filepath in md_files:
            fixed, changes = fix_tilde_in_times(filepath)
            if fixed:
                total_fixed += 1
                stats[lang] += 1
                print(f"✓ Fixed: {filepath.name} ({lang.upper()})")
                for change in changes:
                    print(change)
                print()
    
    print(f"{'='*60}")
    print(f"Summary:")
    print(f"  Total files fixed: {total_fixed}")
    print(f"  EN: {stats['en']} files")
    print(f"  JA: {stats['ja']} files")
    print(f"  ZH-CN: {stats['zh-cn']} files")
    print(f"{'='*60}")
    
    if total_fixed == 0:
        print("\n✅ All blog posts are already properly formatted!")

if __name__ == '__main__':
    main()
