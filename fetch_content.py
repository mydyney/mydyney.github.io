import requests
import sys

url = "https://blog.naver.com/PostView.naver?blogId=tokyomate&logNo=224035271300"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    with open("NaverBlogViewer.txt", "w", encoding="utf-8") as f:
        f.write(response.text)
    
    print(f"Successfully downloaded {len(response.text)} bytes to NaverBlogViewer.txt")

except Exception as e:
    print(f"Error fetching content: {e}")
    sys.exit(1)
