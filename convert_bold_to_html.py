#!/usr/bin/env python3
"""
Convert Markdown bold syntax (**text**) to HTML <strong> tags in all blog posts.
This ensures consistent rendering within <div class="blog-container"> blocks.
"""

import os
import re
from pathlib import Path

def convert_bold_syntax(content):
    """
    Convert **text** to <strong>text</strong>
    
    Pattern explanation:
    - \*\* : Match literal **
    - ([^*\n]+?) : Capture group - one or more chars that are not * or newline (non-greedy)
    - \*\* : Match closing **
    
    This avoids matching across multiple lines or capturing ** in other contexts.
    """
    # Pattern to match **text** but not *** (which might be heading or separator)
    pattern = r'\*\*([^*\n]+?)\*\*'
    replacement = r'<strong>\1</strong>'
    
    new_content = re.sub(pattern, replacement, content)
    return new_content

def process_file(filepath):
    """Process a single markdown file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        new_content = convert_bold_syntax(original_content)
        
        # Check if any changes were made
        if original_content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            # Count number of replacements
            original_count = original_content.count('**')
            new_count = new_content.count('**')
            replacements = (original_count - new_count) // 2
            
            return True, replacements
        return False, 0
        
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False, 0

def main():
    """Process all blog post markdown files"""
    
    # Find all markdown files in content directories
    content_dirs = ['content/en/posts', 'content/ja/posts', 'content/zh-cn/posts']
    
    total_files_changed = 0
    total_replacements = 0
    files_by_lang = {'en': 0, 'ja': 0, 'zh-cn': 0}
    
    for content_dir in content_dirs:
        if not os.path.exists(content_dir):
            continue
            
        lang = 'en' if '/en/' in content_dir else ('ja' if '/ja/' in content_dir else 'zh-cn')
        
        md_files = list(Path(content_dir).glob('*.md'))
        
        for filepath in md_files:
            changed, count = process_file(filepath)
            if changed:
                total_files_changed += 1
                total_replacements += count
                files_by_lang[lang] += 1
                print(f"✓ {filepath.name}: {count} replacements")
    
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Total files changed: {total_files_changed}")
    print(f"  Total **bold** → <strong>bold</strong> replacements: {total_replacements}")
    print(f"  By language:")
    print(f"    EN: {files_by_lang['en']} files")
    print(f"    JA: {files_by_lang['ja']} files")
    print(f"    ZH-CN: {files_by_lang['zh-cn']} files")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
