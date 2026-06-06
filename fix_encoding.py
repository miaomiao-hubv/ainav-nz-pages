import re

with open(r'D:\ainav-nz-pages\rent-vs-buy.html', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Fix the zh-signoff p tag - use regex to find the line with any corrupted content
pattern = r'<p class="zh-signoff">[^<]*</p>'
replacement = '<p class="zh-signoff">希望兰局早日登录纽西兰</p>'
content = re.sub(pattern, replacement, content)

with open(r'D:\ainav-nz-pages\rent-vs-buy.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed zh-signoff line')
