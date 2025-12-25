#!/usr/bin/env python3
"""Remove duplicate Editor's Note sections from all blog posts"""

import os
from pathlib import Path

def remove_duplicate_editors_note(filepath):
    """Remove duplicate Editor's Note sections"""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Find all lines with '<div class="editors-note">'
    editors_note_indices = []
    for i, line in enumerate(lines):
        if '<div class="editors-note">' in line:
            editors_note_indices.append(i)
    
    if len(editors_note_indices) > 1:
        # Remove all duplicates except the first one
        # Work backwards to preserve line indices
        for start_idx in reversed(editors_note_indices[1:]):
            # Editor's Note structure is typically 5 lines:
            # <div class="editors-note">
            #   <p ...><strong>Editor's Note</strong></p>
            #   <p ...>content</p>
            # </div>
            # Plus blank lines before/after
            
            # Find the closing </div> for this section
            end_idx = start_idx
            for i in range(start_idx, min(start_idx + 10, len(lines))):
                if '</div>' in lines[i]:
                    end_idx = i
                    break
            
            # Remove blank line before if exists
            if start_idx > 0 and lines[start_idx - 1].strip() == '':
                start_remove = start_idx - 1
            else:
                start_remove = start_idx
            
            # Remove the duplicate section
            del lines[start_remove:end_idx + 1]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        
        return True
    
    return False

def main():
    """Process all blog posts with duplicate Editor's Notes"""
    
    content_dirs = ['content/en/posts', 'content/ja/posts', 'content/zh-cn/posts']
    
    fixed_count = 0
    stats = {'en': 0, 'ja': 0, 'zh-cn': 0}
    
    for content_dir in content_dirs:
        if not os.path.exists(content_dir):
            continue
        
        lang = 'en' if '/en/' in content_dir else ('ja' if '/ja/' in content_dir else 'zh-cn')
        
        md_files = list(Path(content_dir).glob('*.md'))
        
        for filepath in md_files:
            if remove_duplicate_editors_note(filepath):
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
