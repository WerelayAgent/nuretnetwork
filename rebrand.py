import os
import re

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    original = content
    
    # Text replacements
    content = content.replace("Nur Network", "Nuret Network")
    content = content.replace("Nur", "Nuret")
    content = content.replace("nur", "nuret")
    content = content.replace("NUR", "NURET")
    
    # Need to be careful because replacing "nur" might replace "nuret" again if we run twice, but this is a fresh folder
    
    # Twitter
    content = re.sub(r'https?://(?:twitter\.com|x\.com)/[a-zA-Z0-9_]+', 'https://x.com/nuretnetwork', content)
    
    # Contract Address
    content = content.replace("8oYncHSbnkqyY63G6kfrfFkoxcTa3MW7UBRJu6A7pump", "coming soon on pump.fun")
    
    # Fix potential over-replacements
    # E.g., if it replaced nurnetwork.org to nuretnetwork.org, that's fine.
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Patched {filepath}")

for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith(('.html', '.js', '.css')):
            replace_in_file(os.path.join(root, file))
