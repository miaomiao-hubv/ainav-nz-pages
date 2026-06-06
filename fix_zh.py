import re

with open(r'D:\ainav-nz-pages\rent-vs-buy.html', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Replace the corrupted zh-signoff line
old = '<p class="zh-signoff">希望兰局早日登录纽西�?/p>'
new = '<p class="zh-signoff">希望兰局早日登录纽西兰</p>'
content = content.replace(old, new)

# Also try finding by regex in case the corruption is different
content = re.sub(
    r'<p class="zh-signoff">[^<]*</p>',
    '<p class="zh-signoff">希望兰局早日登录纽西兰</p>',
    content
)

with open(r'D:\ainav-nz-pages\rent-vs-buy.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed zh-signoff')
