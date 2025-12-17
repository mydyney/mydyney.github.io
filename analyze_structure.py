#!/usr/bin/env python3
"""
Analyze Naver blog HTML structure to extract:
- Publish date
- All text content with headings
- Tables and their positions
- Images and their positions (including groups)
- Captions
- Links
"""

import re
from bs4 import BeautifulSoup

def analyze_naver_html(filename='naver.html'):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # Extract publish date
    publish_date_elem = soup.find('span', class_='se_publishDate')
    if publish_date_elem:
        publish_date = publish_date_elem.text.strip()
        print(f"📅 Publish Date: {publish_date}")
        print()
    
    # Find all se-components in order
    components = soup.find_all('div', class_=re.compile(r'se-component'))
    
    print(f"📊 Total Components: {len(components)}")
    print("="*80)
    print()
    
    position = 0
    for idx, component in enumerate(components, 1):
        component_classes = component.get('class', [])
        
        # Skip certain components
        if 'se-documentTitle' in component_classes or 'se-oglink' in component_classes:
            continue
            
        position += 1
        
        # Check component type
        if 'se-sectionTitle' in component_classes:
            text_elem = component.find('p', class_='se-text-paragraph')
            if text_elem:
                text = text_elem.get_text(strip=True)
                print(f"[{position}] 📌 SECTION TITLE")
                print(f"    Text: {text}")
                print()
                
        elif 'se-text' in component_classes:
            paragraphs = component.find_all('p', class_='se-text-paragraph')
            if paragraphs:
                print(f"[{position}] 📝 TEXT")
                for p in paragraphs:
                    text = p.get_text(strip=True)
                    # Check for links
                    links = p.find_all('a', class_='se-link')
                    if links:
                        print(f"    Text with {len(links)} link(s): {text[:100]}...")
                        for link in links:
                            print(f"      🔗 {link.get('href', 'N/A')}")
                    else:
                        print(f"    {text[:100]}...")
                print()
                
        elif 'se-image' in component_classes:
            images = component.find_all('img')
            captions = component.find_all('div', class_='se-caption')
            
            if len(images) > 1:
                print(f"[{position}] 🖼️ IMAGE GROUP ({len(images)} images)")
            else:
                print(f"[{position}] 🖼️ IMAGE")
                
            for img_idx, img in enumerate(images, 1):
                img_src = img.get('data-lazy-src') or img.get('src', 'N/A')
                print(f"    Image {img_idx}: {img_src[:80]}...")
                
            if captions:
                for cap_idx, caption in enumerate(captions, 1):
                    cap_text = caption.get_text(strip=True)
                    # Check for links in caption
                    cap_links = caption.find_all('a')
                    if cap_links:
                        print(f"    Caption {cap_idx}: {cap_text} (with link)")
                    else:
                        print(f"    Caption {cap_idx}: {cap_text}")
            print()
            
        elif 'se-table' in component_classes:
            print(f"[{position}] 📊 TABLE")
            table = component.find('table')
            if table:
                rows = table.find_all('tr')
                print(f"    Rows: {len(rows)}")
                # Show first row as sample
                if rows:
                    first_row = rows[0]
                    cells = first_row.find_all(['th', 'td'])
                    cell_texts = [cell.get_text(strip=True) for cell in cells]
                    print(f"    First row: {' | '.join(cell_texts)}")
            print()
            
        elif 'se-horizontalLine' in component_classes:
            print(f"[{position}] ➖ HORIZONTAL LINE")
            print()
            
        elif 'se-sticker' in component_classes:
            print(f"[{position}] 😊 STICKER/EMOJI")
            print()

if __name__ == '__main__':
    analyze_naver_html()
