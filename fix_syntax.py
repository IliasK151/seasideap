import re

with open('/Users/eliaskotsias/Desktop/Seaside Photos/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# removing stray syntax
text = re.sub(r'\);\s*}\s*(calSelection = \[ci, co\];)', r'\1', text)

with open('/Users/eliaskotsias/Desktop/Seaside Photos/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Syntax fixed")
