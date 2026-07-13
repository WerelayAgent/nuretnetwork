import os

filepath = 'assets/index-fH9VZ6Kv.js'
with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Replace the PublicKey instantiation with a valid address
# We assume "me" is the PublicKey class based on the minified source.
# Instead of a regex that might miss, we can just replace 'new me("coming soon on pump.fun")' 
# or similar, but the variable might not be "me" next time if we re-scrape.
# However, we already have the minified file and it's "me".
content = content.replace('new me("coming soon on pump.fun")', 'new me("11111111111111111111111111111111")')

# Let's also check for other minified names just in case
import re
content = re.sub(r'new [a-zA-Z0-9_$]+\("coming soon on pump\.fun"\)', 'new me("11111111111111111111111111111111")', content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Patched PublicKey in {filepath}")
