import os
import re
import requests

BASE_URL = "https://nurnetwork.org"

def download_file(url, local_path):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            with open(local_path, 'wb') as f:
                f.write(r.content)
            print(f"Downloaded: {url} -> {local_path}")
        else:
            print(f"Failed (status {r.status_code}): {url}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def main():
    r = requests.get(BASE_URL)
    html = r.text
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Saved index.html")
    
    # Find all assets
    assets = set()
    assets.update(re.findall(r'href=["\'](/[^"\']+\.(?:css|png|jpg|jpeg|svg|webp|ico|woff|woff2|js))["\']', html))
    assets.update(re.findall(r'src=["\'](/[^"\']+\.(?:css|png|jpg|jpeg|svg|webp|ico|woff|woff2|js))["\']', html))
    assets.update(re.findall(r'href=["\'](\./[^"\']+\.(?:css|png|jpg|jpeg|svg|webp|ico|woff|woff2|js))["\']', html))
    assets.update(re.findall(r'src=["\'](\./[^"\']+\.(?:css|png|jpg|jpeg|svg|webp|ico|woff|woff2|js))["\']', html))
    
    for asset in assets:
        clean_asset = asset.lstrip('.')
        if not clean_asset.startswith('/'):
            clean_asset = '/' + clean_asset
        url = BASE_URL + clean_asset
        local_path = "." + clean_asset
        download_file(url, local_path)

if __name__ == "__main__":
    main()
