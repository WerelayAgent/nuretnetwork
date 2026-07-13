import os

filepath = 'assets/index-fH9VZ6Kv.js'
with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

original = content
content = content.replace('nuret-logo', 'nur-logo')

if content != original:
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Reverted nuret-logo to nur-logo")
else:
    print("No changes made")
