import os
import requests

for root, _, files in os.walk('.'):
    for f in files:
        if f.endswith(('.js', '.css', '.html')) and not f.startswith('rebrand') and not f.startswith('scrape'):
            path = os.path.join(root, f)
            url_path = path.replace('\\', '/').replace('./', '')
            if url_path == 'index.html':
                url = 'https://nurnetwork.org/'
            else:
                url = f'https://nurnetwork.org/{url_path}'
            
            try:
                r = requests.get(url)
                if r.status_code == 200:
                    with open(path, 'wb') as file:
                        file.write(r.content)
                    print(f"Restored {path}")
            except Exception as e:
                pass
