#!/usr/bin/env python3
"""Convert pure Markdown posts to blog-container format"""

import re
from pathlib import Path

# Files to convert (slugs)
POSTS_TO_CONVERT = [
    'miyashita-park-illumination-2024',
    'shibuya-human-made-offline-store-guide',
    'shibuya-parco-kiwamiya-hamburg-waiting-menu',
    'shibuya-station-coin-locker-luggage-storage-guide',
    'shimokitazawa-tokyo-travel-guide',
    'tokyo-station-sawamura-lunch',
    'tokyo-station-year-end-hours-2026',
]

def convert_to_blog_container(filepath):
    """Convert a Markdown post to blog-container format"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has blog-container
    if '<div class="blog-container">' in content:
        return False, "Already has blog-container"
    
    # Split front matter and content
    parts = content.split('---')
    if len(parts) < 3:
        return False, "Invalid front matter"
    
    front_matter = f"---{parts[1]}---"
    body = '---'.join(parts[2:]).lstrip('\n')
    
    # Check if there's an Editor's Note at the end
    editors_note_match = re.search(r'(<div class="editors-note">.*?</div>)\s*$', body, re.DOTALL)
    
    if editors_note_match:
        editors_note = editors_note_match.group(1)
        main_content = body[:editors_note_match.start()].rstrip()
    else:
        editors_note = None
        main_content = body.rstrip()
    
    # Find the first paragraph or content to use as intro
    # Look for the first non-empty line after any initial images/figures
    lines = main_content.split('\n')
    intro_found = False
    intro_text = ""
    
    for i, line in enumerate(lines):
        # Skip empty lines, images, and HTML tags at the start
        if not line.strip() or line.strip().startswith(('<figure', '<img', '##', '#')):
            continue
        # Found first content paragraph
        if line.strip() and not line.strip().startswith('<'):
            intro_text = line.strip()
            intro_found = True
            break
    
    # If no suitable intro found, create a generic one
    if not intro_text:
        intro_text = "Complete guide with all the essential information you need!"
    
    # Build new content
    new_content = front_matter + "\n\n"
    new_content += '<div class="blog-container">\n\n'
    
    # Add styled intro paragraph (use the first paragraph as intro)
    # Remove markdown bold syntax from intro for clean display
    clean_intro = re.sub(r'\*\*(.+?)\*\*', r'\1', intro_text)
    clean_intro = re.sub(r'<strong>(.+?)</strong>', r'\1', clean_intro)
    
    new_content += f'<p style="text-align: center; font-size: 1.1rem; color: #555;">{clean_intro}</p>\n\n'
    
    # Add main content
    new_content += main_content + '\n\n'
    
    # Add Editor's Note if it exists
    if editors_note:
        new_content += editors_note + '\n\n'
    
    # Close blog-container
    new_content += '</div>\n'
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True, "Converted successfully"

def main():
    """Convert all specified posts in all languages"""
    
    languages = ['en', 'ja', 'zh-cn']
    total_converted = 0
    stats = {'en': 0, 'ja': 0, 'zh-cn': 0}
    
    print("Converting pure Markdown posts to blog-container format...\n")
    
    for slug in POSTS_TO_CONVERT:
        print(f"Processing: {slug}")
        
        for lang in languages:
            filepath = Path(f'content/{lang}/posts/{slug}.md')
            
            if not filepath.exists():
                print(f"  ⚠️  {lang.upper()}: File not found")
                continue
            
            success, message = convert_to_blog_container(filepath)
            
            if success:
                total_converted += 1
                stats[lang] += 1
                print(f"  ✓ {lang.upper()}: {message}")
            else:
                print(f"  - {lang.upper()}: {message}")
        
        print()
    
    print(f"{'='*60}")
    print(f"Summary:")
    print(f"  Total files converted: {total_converted}")
    print(f"  EN: {stats['en']} files")
    print(f"  JA: {stats['ja']} files")
    print(f"  ZH-CN: {stats['zh-cn']} files")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
