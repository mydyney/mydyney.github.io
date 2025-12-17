#!/usr/bin/env python3
"""
Naver blog to Hugo markdown converter for Shinjuku Chuo Park
Extracts content, translates, and creates multilingual blog posts
"""

import re
import json
from html import unescape
from datetime import datetime

def clean_text(text):
    """Remove HTML tags and clean text"""
    text = re.sub(r'<[^>]+>', '', text)
    text = unescape(text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_full_content(html_file):
    """Extract all content from Naver HTML"""
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Extract title
    title_match = re.search(r'<p class="se-text-paragraph[^"]*"[^>]*id="SE-156a60ca[^"]*"[^>]*>(.*?)</p>', html, re.DOTALL)
    title = clean_text(title_match.group(1)) if title_match else ""
    
    # Extract all content blocks
    content_blocks = []
    
    # Find all se-module-text divs
    modules = re.findall(r'<div class="se-module se-module-text[^"]*">(.*?)</div>\s*(?:<!--.*?-->)?\s*(?=<div class="se-module|<div class="se-section|$)', html, re.DOTALL)
    
    for module in modules:
        # Extract paragraphs
        paras = re.findall(r'<p class="se-text-paragraph[^"]*"[^>]*>(.*?)</p>', module, re.DOTALL)
        for para in paras:
            text = clean_text(para)
            if text and len(text) > 3:
                is_bold = '<b>' in para or '<strong>' in para or 'font-weight:bold' in para
                is_large = 'font-size:2' in para or 'font-size:3' in para
                
                content_blocks.append({
                    'text': text,
                    'bold': is_bold,
                    'large': is_large
                })
    
    # Extract image captions
    captions = []
    caption_matches = re.findall(r'<figcaption[^>]*>(.*?)</figcaption>', html, re.DOTALL)
    for cap in caption_matches:
        text = clean_text(cap)
        if text:
            captions.append(text)
    
    # Extract Naver links
    naver_links = re.findall(r'href="(https://blog\.naver\.com/tokyomate/\d+)"', html)
    naver_links = list(dict.fromkeys(naver_links))
    
    return {
        'title': title,
        'content_blocks': content_blocks,
        'captions': captions,
        'naver_links': naver_links
    }

if __name__ == '__main__':
    data = extract_full_content('naver.html')
    
    print(f"Title: {data['title']}")
    print(f"Content blocks: {len(data['content_blocks'])}")
    print(f"Captions: {len(data['captions'])}")
    print(f"Naver links: {len(data['naver_links'])}")
    
    # Save to JSON for manual processing
    with open('/tmp/shinjuku_full.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("\nSaved to /tmp/shinjuku_full.json")
