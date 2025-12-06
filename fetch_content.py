import requests
import sys
from bs4 import BeautifulSoup

def fetch_naver_blog(url=None):
    if not url:
        # Default URL if none provided
        url = "https://blog.naver.com/PostView.naver?blogId=tokyomate&logNo=224035271300"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    }

    try:
        print(f"Fetching: {url}")
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Target the specific viewer class
        target_class = "se-viewer se-theme-default"
        # Since classes in BS4 are lists, we can search for it directly or select it
        # Note: css selector logic might handle spaces differently, usually dots.
        # .se-viewer.se-theme-default
        
        content_element = soup.select_one(".se-viewer.se-theme-default")
        
        if content_element:
            html_content = str(content_element)
            filename = "naver.html"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(html_content)
            
            print(f"Successfully extracted content class '{target_class}'")
            print(f"Saved {len(html_content)} bytes to {filename}")
        else:
            print(f"Warning: Could not find element with class '{target_class}'")
            print("Saving full HTML as fallback...")
            with open("naver.html", "w", encoding="utf-8") as f:
                f.write(response.text)

    except Exception as e:
        print(f"Error fetching content: {e}")
        sys.exit(1)

if __name__ == "__main__":
    target_url = sys.argv[1] if len(sys.argv) > 1 else None
    fetch_naver_blog(target_url)
