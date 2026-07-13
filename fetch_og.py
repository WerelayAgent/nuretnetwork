import re, requests

text = open('index.html', 'r', encoding='utf-8').read()
matches = re.findall(r'content=["\'](/[^"\']+\.(?:png|jpg|jpeg|svg|webp|ico|woff|woff2))["\']', text)
for m in matches:
    print("Downloading", m)
    r = requests.get('https://nurnetwork.org' + m)
    with open('.' + m, 'wb') as f:
        f.write(r.content)
