import os

for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith(('.js', '.html', '.css')):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            original = content
            
            # Revert backend API function names
            content = content.replace("nuret-api", "nur-api")
            content = content.replace("nuret-pay-api", "nur-pay-api")
            content = content.replace("nuret-api-keys", "nur-api-keys")
            
            # Revert API domains
            content = content.replace("api.nuretnetwork.org", "api.nurnetwork.org")
            
            if content != original:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Patched backend URLs in {filepath}")
