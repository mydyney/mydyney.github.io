
import sys
from bs4 import BeautifulSoup
import re


def process_text_element(element):
    """
    Recursively extract text with markdown links.
    """
    if element.name == 'a':
        href = element.get('href', '')
        text = element.get_text(strip=True)
        if href and text:
            return f"[{text}]({href})"
        return text
    
    if element.name == 'span' or element.name == 'p' or element.name == 'div':
        # Process children
        content = ""
        for child in element.children:
            if child.name:
                content += process_text_element(child)
            else:
                content += child.string if child.string else ""
        return content

    return element.get_text() if element.get_text() else ""

def clean_text_with_links(element):
    # This function replaces the simple clean_text
    # It parses the HTML content of the paragraph to preserve <a> tags
    
    # Check for direct text
    if not element.contents:
        return ""
    
    result = []
    for child in element.contents:
        if child.name == 'a':
            href = child.get('href')
            text = child.get_text(strip=True)
            if href:
                # Naver internal links often have strange attributes, but href is usually valid or data-linkdata
                # Sometimes href="#" and data-linkdata has the url.
                if href == '#' and child.get('data-linkdata'):
                     import json
                     try:
                        data = json.loads(child.get('data-linkdata'))
                        href = data.get('link', '#')
                     except:
                        pass
                
                result.append(f"[{text}]({href})")
            else:
                result.append(text)
        elif child.name == 'span':
             # Recursively handle spans which might contain 'a' tags or just text
             result.append(clean_text_with_links(child))
        elif child.name == 'br':
            result.append("\n")
        elif child.string:
            result.append(child.string)
    
    # Join and clean up
    text = "".join(result).strip()
    return text

def html_table_to_md(table_div):
    # Improved table extractor
    rows = []
    # Find the table element inside
    table = table_div.find('table')
    if not table:
        return ""

    for tr in table.find_all('tr'):
        cells = []
        for td in tr.find_all(['td', 'th']):
            # Use the link-preserving cleaner for cells too
            cells.append(clean_text_with_links(td).replace('\n', '<br>')) 
        rows.append(cells)

    if not rows:
        return ""

    num_cols = max(len(r) for r in rows)
    
    normalized_rows = []
    for r in rows:
        r += [""] * (num_cols - len(r))
        normalized_rows.append(r)
    
    md_lines = []
    
    # Header
    # If the first row is just data, we still need a header for MD tables usually, 
    # but we can just use the first row as header.
    header = normalized_rows[0]
    md_lines.append("| " + " | ".join(header) + " |")
    md_lines.append("| " + " | ".join(["---"] * num_cols) + " |")
    
    for row in normalized_rows[1:]:
        md_lines.append("| " + " | ".join(row) + " |")
        
    return "\n".join(md_lines)

def convert_to_md(html_file, slug):
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    main_container = soup.select_one('.se-main-container')
    if not main_container:
        print("Error: No se-main-container found")
        return ""

    img_count = 0
    markdown_output = []

    for element in main_container.find_all(recursive=False):
        # Text
        if 'se-text' in element.get('class', []):
            paragraphs = element.select('.se-text-paragraph')
            for p in paragraphs:
                # Use new cleaner with link support
                text = clean_text_with_links(p)
                if text:
                    # Basic header detection (naive)
                    if p.find('b') and len(text) < 60 and not text.startswith('['):
                         markdown_output.append(f"### {text}\n")
                    else:
                         markdown_output.append(f"{text}\n")
            markdown_output.append("\n")

        # Section Title
        elif 'se-sectionTitle' in element.get('class', []):
            text = clean_text_with_links(element)
            markdown_output.append(f"## {text}\n\n")

        # Image (Single)
        elif 'se-image' in element.get('class', []):
            imgs = element.select('img.se-image-resource')
            for img in imgs:
                img_count += 1
                caption = ""
                caption_div = element.select_one('.se-caption')
                if caption_div:
                    caption = caption_div.get_text(strip=True)
                
                md_img = f'![{caption}](/images/posts/{slug}-{img_count:02d}.jpg)'
                # Add caption below
                if caption:
                    md_img += f'\n<p class="image-caption">{caption}</p>'
                markdown_output.append(md_img + "\n\n")

        # Image Group (Collage/Slide)
        elif 'se-imageGroup' in element.get('class', []):
            imgs = element.select('img.se-image-resource')
            caption = ""
            caption_div = element.select_one('.se-caption')
            if caption_div:
                caption = caption_div.get_text(strip=True)

            # For groups, we'll just stack them for now
            for i, img in enumerate(imgs):
                img_count += 1
                md_img = f'![{caption}](/images/posts/{slug}-{img_count:02d}.jpg)'
                markdown_output.append(md_img + "\n")
            
            if caption:
                markdown_output.append(f'<p class="image-caption">{caption}</p>\n')
            markdown_output.append("\n")

        # Table
        elif 'se-table' in element.get('class', []):
            md_table = html_table_to_md(element)
            markdown_output.append(md_table + "\n\n")

        # Horizontal Line
        elif 'se-horizontalLine' in element.get('class', []):
            markdown_output.append("---\n\n")

        # Link (Oembed/Sticker) - e.g. "Together with" links
        elif 'se-oglink' in element.get('class', []):
             # These are large link cards. extract url and title
             link_div = element.select_one('a.se-oglink-info')
             if link_div:
                 href = link_div.get('href')
                 title = link_div.select_one('.se-oglink-title')
                 title_text = title.get_text(strip=True) if title else "Read More"
                 markdown_output.append(f"> **[{title_text}]({href})**\n\n")

    return "".join(markdown_output)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 convert_naver_to_md.py <html_file> <slug>")
        sys.exit(1)
    
    print(convert_to_md(sys.argv[1], sys.argv[2]))
