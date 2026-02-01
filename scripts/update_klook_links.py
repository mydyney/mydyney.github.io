import os
import re
import urllib.parse

# Tripmate Template IDs
NEW_AID = "110453"
NEW_AFF_ADID = "1208343"

# Localization Mapping
LOCALES = {
    "en": {"path": "/en-US/", "currency": "USD"},
    "ja": {"path": "/ja/", "currency": "JPY"},
    "zh-cn": {"path": "/zh-CN/", "currency": "CNY"},
}

# Regex to find Klook affiliate links
# Captures aid, aff_adid, and k_site
KLOOK_REGEX = re.compile(r'https://affiliate\.klook\.com/redirect\?[^"\'>\s]+')

def update_link(match, lang):
    url = match.group(0)
    parsed = urllib.parse.urlparse(url)
    params = urllib.parse.parse_qs(parsed.query)
    
    if "k_site" not in params:
        return url
        
    k_site = params["k_site"][0]
    
    # Localize k_site
    # Replace language paths like /ko/, /en-US/, etc. with the target locale path
    locale_info = LOCALES.get(lang)
    if not locale_info:
        return url
        
    # Standardize path
    # Replace existing language identifiers (/ko/, /en-US/, /ja/, /zh-CN/) with target
    # This assumes the destination URL is a klook.com domain
    k_site_parsed = urllib.parse.urlparse(k_site)
    path = k_site_parsed.path
    
    # List of known klook language prefixes to replace
    for prefix in ["/ko/", "/en-US/", "/ja/", "/zh-CN/", "/zh-TW/", "/en-AU/"]:
        if path.startswith(prefix):
            path = path.replace(prefix, locale_info["path"], 1)
            break
    else:
        # If no known prefix found, prepend the target prefix if it's missing
        if not path.startswith(locale_info["path"]):
            path = locale_info["path"] + path.lstrip("/")

    # Update/Add currency parameter in k_site
    k_site_params = urllib.parse.parse_qs(k_site_parsed.query)
    k_site_params["currency"] = [locale_info["currency"]]
    
    # Remove any tracking noise from k_site (standardize)
    for noise in ["clickId", "aff_klick_id", "utm_source", "utm_medium", "utm_campaign"]:
        if noise in k_site_params:
            del k_site_params[noise]
            
    # Rebuild k_site
    new_k_site_query = urllib.parse.urlencode(k_site_params, doseq=True)
    new_k_site = urllib.parse.urlunparse(k_site_parsed._replace(path=path, query=new_k_site_query))
    
    # Rebuild Wrapper with new Tripmate IDs
    new_wrapper_params = {
        "aid": NEW_AID,
        "aff_adid": NEW_AFF_ADID,
        "utm_source": "tripmate",
        "utm_campaign": "bulk-update-2026",
        "k_site": new_k_site
    }
    
    new_url = f"https://affiliate.klook.com/redirect?{urllib.parse.urlencode(new_wrapper_params)}"
    return new_url

def process_directory(base_dir):
    for lang in ["en", "ja", "zh-cn"]:
        dir_path = os.path.join(base_dir, lang, "posts")
        if not os.path.exists(dir_path):
            continue
            
        print(f"Processing {lang} posts...")
        for filename in os.listdir(dir_path):
            if filename.endswith(".md"):
                file_path = os.path.join(dir_path, filename)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # Perform substitution
                new_content = KLOOK_REGEX.sub(lambda m: update_link(m, lang), content)
                
                if new_content != content:
                    print(f"  Updated: {filename}")
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)

if __name__ == "__main__":
    CONTENT_DIR = "/Users/tommygo/Desktop/personal-project/mydyney.github.io/content"
    process_directory(CONTENT_DIR)
    print("Done!")
