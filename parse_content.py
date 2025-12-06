import re
import os

def parse_naver_blog(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract title
    title_match = re.search(r'<title>(.*?)</title>', content)
    title = title_match.group(1) if title_match else "No Title"
    print(f"Title: {title}")

    # Extract date - usually in <span class="se_publishDate">
    date_match = re.search(r'class="se_publishDate pcol2">(.*?)</span>', content)
    date_str = date_match.group(1) if date_match else "2025-10-09" # Fallback
    print(f"Date: {date_str}")

    # Extract main content using "se-module-text" or "se-module-image"
    # This is a specialized parser for Naver SmartEditor
    
    # We will look for <p class="se-text-paragraph ...">(.*?)</p> for text
    # AND <img ... src="(.*?)" ...> inside "se-module-image" for images
    
    # To preserve order, we can iterate through the file finding modules
    # But regex for whole file is tricky. 
    # Let's split by "se-component" divs which represent blocks.
    
    components = re.findall(r'<div class="se-component (.*?)" id=".*?">(.*?)</div>\s*</div>\s*</div>', content, re.DOTALL)
    
    # Create output markdown
    markdown_lines = []
    
    image_count = 0
    
    for comp_class, comp_content in components:
        # Check type
        if "se-text" in comp_class or "se-sectionTitle" in comp_class:
            # Extract text
            paragraphs = re.findall(r'<span.*?>(.*?)</span>', comp_content, re.DOTALL)
            text_block = ""
            for p in paragraphs:
                # Remove HTML tags inside span if any
                clean_p = re.sub(r'<.*?>', '', p).strip()
                # Handle special chars
                clean_p = clean_p.replace('&nbsp;', ' ').replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
                if clean_p:
                     text_block += clean_p + "\n"
            
            if text_block:
                markdown_lines.append(f"TEXT: {text_block}")

        elif "se-image" in comp_class:
            # Extract image src
            img_match = re.search(r'src="(https://postfiles\.pstatic\.net/[^"]+)"', comp_content)
            if img_match:
                img_url = img_match.group(1)
                # Cleaning url parameters
                img_url = img_url.split('?')[0]
                image_count += 1
                markdown_lines.append(f"IMAGE: {img_url} (Local: shinjuku-guide-2025-{image_count:02d}.jpg)")
                
                # Check for caption
                caption_match = re.search(r'se-caption.*?<span.*?>(.*?)</span>', comp_content, re.DOTALL)
                if caption_match:
                     caption = re.sub(r'<.*?>', '', caption_match.group(1)).strip()
                     markdown_lines.append(f"CAPTION: {caption}")

        elif "se-table" in comp_class:
             markdown_lines.append("TABLE: [Table detected, handle manually]")
             
    with open("parsed_content.txt", "w", encoding="utf-8") as f:
        for line in markdown_lines:
            f.write(line + "\n")
            
    print(f"Parsed {len(markdown_lines)} items. Saved to parsed_content.txt")

parse_naver_blog('NaverBlogViewer.txt')
