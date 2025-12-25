#!/usr/bin/env python3
"""Check for duplicate Editor's Note sections in all blog posts"""

import os
from pathlib import Path

def check_file(filepath):
    """Check if a file has duplicate Editor's Note"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count occurrences of editors-note div
    count = content.count('<div class="editors-note">')
    
    if count > 1:
        return True, count
    return False, count

def main():
    """Scan all blog posts for duplicate Editor's Notes"""
    
    content_dirs = ['content/en/posts', 'content/ja/posts', 'content/zh-cn/posts']
    
    duplicates = []
    stats = {'en': 0, 'ja': 0, 'zh-cn': 0}
    
    for content_dir in content_dirs:
        if not os.path.exists(content_dir):
            continue
        
        lang = 'en' if '/en/' in content_dir else ('ja' if '/ja/' in content_dir else 'zh-cn')
        
        md_files = list(Path(content_dir).glob('*.md'))
        
        for filepath in md_files:
            has_duplicate, count = check_file(filepath)
            if has_duplicate:
                duplicates.append({
                    'file': str(filepath),
                    'lang': lang,
                    'count': count,
                    'name': filepath.name
                })
                stats[lang] += 1
    
    # Print results
    if duplicates:
        print(f"❌ Found {len(duplicates)} files with duplicate Editor's Note:\n")
        
        for item in duplicates:
            print(f"  {item['lang'].upper()}: {item['name']} ({item['count']} occurrences)")
        
        print(f"\n{'='*60}")
        print(f"Summary by language:")
        print(f"  EN: {stats['en']} files")
        print(f"  JA: {stats['ja']} files")
        print(f"  ZH-CN: {stats['zh-cn']} files")
        print(f"  Total: {len(duplicates)} files")
        print(f"{'='*60}")
    else:
        print("✅ No duplicate Editor's Notes found!")
    
    return duplicates

if __name__ == '__main__':
    duplicates = main()
