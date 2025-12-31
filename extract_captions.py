from bs4 import BeautifulSoup
import re

with open("naver.md", "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

# Find all components to maintain linear order
components = soup.find_all("div", class_=re.compile(r"se-component"))

img_index = 1
for comp in components:
    # Check for image or image group
    if "se-image" in comp.get("class", []):
        img = comp.find("img")
        if img:
            src = img.get("src", "")
            # Naver structure for caption is often a sibling module
            caption = ""
            caption_module = comp.find("div", class_=re.compile(r"se-caption"))
            if caption_module:
                caption = caption_module.get_text(strip=True)
            
            print(f"Image {img_index:02d}: {src[:40]}...")
            print(f"  Caption: {caption if caption else '[NONE]'}")
            img_index += 1
            
    elif "se-imageGroup" in comp.get("class", []):
        imgs = comp.find_all("img")
        print(f"--- Image Group Start ({len(imgs)} images) ---")
        for img in imgs:
            src = img.get("src", "")
            # individual captions in groups are tricky, let's look for se-caption within the same parent of img
            img_module = img.find_parent("div", class_=re.compile(r"se-module-image"))
            caption = ""
            if img_module:
                # In groups, captions might be in a parallel module
                next_mod = img_module.find_next_sibling("div", class_=re.compile(r"se-caption"))
                if next_mod:
                    caption = next_mod.get_text(strip=True)
            
            print(f"  Image {img_index:02d}: {src[:40]}...")
            print(f"    Caption: {caption if caption else '[NONE]'}")
            img_index += 1
        print("--- Image Group End ---")
