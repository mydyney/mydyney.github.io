#!/usr/bin/env python3
"""Find all blog posts with <del> tags"""

import os
from pathlib import Path
import re

def find_del_tags(filepath):
    """Find <del> tags and their context"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all <del> tags with context
    pattern = r'.{0,50}<del>(.+?)</del>.{0,50}'
    matches = re.findall(pattern, content, re.DOTALL)
    
    if matches:
        return matches
    return None

def main():
    """Scan all blog posts for <del> tags"""
    
    content_dirs = ['content/en/posts', 'content/ja/posts', 'content/zh-cn/posts']
    
    files_with_del = []
    
    for content_dir in content_dirs:
        if not os.path.exists(content_dir):
            continue
        
        lang = 'en' if '/en/' in content_dir else ('ja' if '/ja/' in content_dir else 'zh-cn')
        
        md_files = list(Path(content_dir).glob('*.md'))
        
        for filepath in md_files:
            matches = find_del_tags(filepath)
            if matches:
                files_with_del.append({
                    'file': filepath.name,
                    'lang': lang,
                    'matches': matches,
                    'count': len(matches)
                })
    
    # Print results
    if files_with_del:
        print(f"❌ Found {len(files_with_del)} files with <del> tags:\n")
        
        for item in files_with_del:
            print(f"\n{'='*70}")
            print(f"File: {item['file']} ({item['lang'].upper()})")
            print(f"<del> tags found: {item['count']}")
            print(f"{'='*70}")
            
            for i, match in enumerate(item['matches'], 1):
                # Clean up the match for display
                clean_match = match.strip().replace('\n', ' ')[:100]
                print(f"  {i}. <del>{clean_match}...</del>")
        
        print(f"\n{'='*70}")
        print(f"Total files with <del> tags: {len(files_with_del)}")
        print(f"{'='*70}")
    else:
        print("✅ No <del> tags found in any blog posts!")

if __name__ == '__main__':
    main()
