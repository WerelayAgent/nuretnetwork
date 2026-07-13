import re
with open('assets/index-fH9VZ6Kv.js', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

imports = re.findall(r'import\([\'"](\./[^\'"]+)[\'"]\)', text)
print(imports)
