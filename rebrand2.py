import os
import re

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    original = content
    
    # Safely replace isolated "Nur"
    # This turns "Nur Network" -> "Nuret Network"
    # and "$nur" -> "$nuret"
    content = re.sub(r'\bNur\b', 'Nuret', content)
    content = re.sub(r'\bnur\b', 'nuret', content)
    content = re.sub(r'\bNUR\b', 'NURET', content)
    
    # Replace combined words if any
    content = content.replace("nurnetwork", "nuretnetwork")
    content = content.replace("NurNetwork", "NuretNetwork")
    
    # Twitter
    content = re.sub(r'https?://(?:twitter\.com|x\.com)/[a-zA-Z0-9_]+', 'https://x.com/nuretnetwork', content)
    
    # Contract Address
    content = content.replace("8oYncHSbnkqyY63G6kfrfFkoxcTa3MW7UBRJu6A7pump", "coming soon on pump.fun")
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Patched {filepath}")

for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith(('.html', '.js', '.css')):
            replace_in_file(os.path.join(root, file))
