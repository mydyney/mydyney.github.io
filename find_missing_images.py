import re

def find_missing_images(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find known images in se-module-image-link
    # We look for the "src" : "URL" pattern inside data-linkdata
    known_images = set()
    # Pattern for data-linkdata
    # data-linkdata='{... "src" : "URL", ...}'
    # This might be multiline or messy, so let's be careful.
    
    # Let's just Regex for all "src" : "..." inside the file first, then filter.
    # Actually, Naver stores it in JSON inside attribute.
    
    # Strategy: Find all https://postfiles.pstatic.net URLs in the file.
    # Clean them (remove query params).
    # Then see which ones appear inside `class="se-module-image-link ..."` blocks vs which ones don't.
    
    all_urls = re.findall(r'https://postfiles\.pstatic\.net/[^"\'\s]+', content)
    unique_base_urls = set()
    for url in all_urls:
        base = url.split('?')[0]  # Remove query params
        if base.endswith('.jpg') or base.endswith('.png') or base.endswith('.gif') or base.endswith('.jpeg'):
            unique_base_urls.add(base)
            
    print(f"Total unique image URLs found in file: {len(unique_base_urls)}")
    
    # Now let's try to see which ones are associated with what context.
    # We will iterate through the file line by line for simplicity to find context.
    
    url_contexts = {}
    
    lines = content.split('\n')
    for i, line in enumerate(lines):
        urls = re.findall(r'https://postfiles\.pstatic\.net/[^"\'\s]+', line)
        for url in urls:
            base = url.split('?')[0]
            if base in unique_base_urls:
                if base not in url_contexts:
                    url_contexts[base] = []
                # Store the line and maybe class info if present on the line
                context = line.strip()[:200] # Truncate for display
                url_contexts[base].append(f"Line {i}: {context}")

    # Now let's see if we have more than 21.
    sorted_urls = sorted(list(unique_base_urls))
    
    print("-" * 50)
    for i, url in enumerate(sorted_urls):
        print(f"Image {i+1}: {url}")
        # Print first context
        if url in url_contexts:
             print(f"  Context: {url_contexts[url][0]}")
             if len(url_contexts[url]) > 1:
                 print(f"  (Found {len(url_contexts[url])} times)")

find_missing_images('NaverBlogViewer.txt')
