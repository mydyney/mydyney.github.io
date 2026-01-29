import re

def extract_images():
    with open('naver.md', 'r') as f:
        content = f.read()
    
    # Regex to find data-linkdata json and extract src
    # This pattern looks for data-linkdata="{...}" and extracts the src inside it
    # We use a non-greedy match for the content to handle multiple matches
    matches = re.findall(r'data-linkdata="([^"]*)"', content)
    
    image_entries = []
    
    print("Found potential linkdata entries:", len(matches))
    
    for i, match in enumerate(matches):
        # Unescape html entities if needed, but usually src is plain url
        src_match = re.search(r'&quot;src&quot;\s*:\s*&quot;([^&]*)&quot;', match)
        if src_match:
            url = src_match.group(1)
            # Append high-res param
            if '?' in url:
                url = url.split('?')[0]
            url = url + '?type=w966'
            image_entries.append(url)
            print(f"Image {len(image_entries)}: {url}")
            
    # Generate curl commands
    slug = "tokyo-moheji-monjayaki-marunouchi-guide"
    commands = []
    for i, url in enumerate(image_entries):
        filename = f"{slug}-{i+1:02d}.jpg"
        cmd = f'curl "{url}" -o static/images/posts/{filename}'
        commands.append(cmd)
        
    with open('download_all_images.sh', 'w') as f:
        f.write("#!/bin/bash\n")
        f.write("mkdir -p static/images/posts\n")
        f.write("\n".join(commands))
        
    print(f"Generated {len(commands)} download commands in download_all_images.sh")

extract_images()
