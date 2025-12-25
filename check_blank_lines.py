import os
import re

def check_blank_line_after_div(filepath):
    """Check if there's a blank line after <div class="blog-container">"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find <div class="blog-container">
    pattern = r'<div class="blog-container">\n(.)'
    match = re.search(pattern, content)
    
    if match:
        # Check if the next character is a newline (blank line)
        next_char = match.group(1)
        if next_char != '\n':
            return filepath
    return None

# Find all markdown files
files_without_blank = []
for root, dirs, files in os.walk('content'):
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            result = check_blank_line_after_div(filepath)
            if result:
                files_without_blank.append(result)

print(f"Files without blank line after blog-container: {len(files_without_blank)}")
for f in files_without_blank:
    print(f)
