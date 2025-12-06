import re

def extract_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all links to tokyomate blog
    # Pattern: https://blog.naver.com/tokyomate/([0-9]+)
    
    # We need to look inside the data-url attributes or href attributes.
    # Naver editor often escapes them, but regex should find them if they are simple.
    
    links = re.findall(r'blog\.naver\.com/tokyomate/([0-9]+)', content)
    
    unique_links = sorted(list(set(links)))
    
    print(f"Found {len(unique_links)} unique Post IDs referenced:")
    for link in unique_links:
        print(f"ID: {link}")

extract_links('NaverBlogViewer.txt')
