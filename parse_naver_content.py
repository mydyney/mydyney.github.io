from bs4 import BeautifulSoup
import sys
import re

try:
    with open('naver.md', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    main_container = soup.find('div', class_='se-main-container')
    if not main_container:
        # Fallback for some old naver styles
        main_container = soup.find('div', id='postViewArea')

    if not main_container:
        print("Error: Could not find main content container")
        sys.exit(1)

    print("--- START CONTENT ---")
    
    # Iterate through all standard Naver modules
    # Common modules: se-module-text, se-module-image, se-module-code, etc.
    
    # We will iterate through children of the main container or find specific classes
    # Naver smart editor 3.0 uses 'se-component' wrapper
    
    components = main_container.find_all(class_='se-component')
    
    img_count = 0
    
    for comp in components:
        # Check component type
        classes = comp.get('class', [])
        
        # TEXT
        if 'se-text' in classes or 'se-sectionTitle' in classes:
            paragraphs = comp.find_all('p')
            for p in paragraphs:
                text = p.get_text().strip()
                if text:
                    # check for links
                    links = p.find_all('a')
                    link_info = ""
                    for link in links:
                        link_info += f" [LINK: {link.get_text()} -> {link.get('href')}]"
                    print(f"[TEXT] {text}{link_info}")
                elif p.find('br'): # Empty line
                    print("[BR]")
                    
        # IMAGE
        elif 'se-image' in classes or 'se-imageStrip' in classes:
            imgs = comp.find_all('img')
            for img in imgs:
                img_count += 1
                src = img.get('data-src') or img.get('src')
                print(f"[IMAGE {img_count:02d}] Source: {src}")
                
            # Caption
            caption = comp.find(class_='se-caption')
            if caption:
                print(f"[CAPTION] {caption.get_text().strip()}")
                
        # HORIZONTAL LINE
        elif 'se-horizontalLine' in classes:
            print("[HR]")
            
        # QUOTE
        elif 'se-quotation' in classes:
            quote = comp.find(class_='se-quote-content')
            if quote:
                print(f"[QUOTE] {quote.get_text().strip()}")
                
        # TABLE
        elif 'se-table' in classes:
            print("[TABLE FOUND - manual extraction needed]")
            
    print("--- END CONTENT ---")

except Exception as e:
    print(f"Error parsing: {e}")
