import re
with open('assets/index-fH9VZ6Kv.js', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

logos = re.findall(r'https?://[^\'"]*logo[^\'"]*', text, flags=re.IGNORECASE)
print(logos)
