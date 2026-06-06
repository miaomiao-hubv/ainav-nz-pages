import re, os

# Correct SVG from index.html (with href for sub-pages)
correct_sidehead = '''  <div class="side-head">
    <a class="side-brand" href="index.html" title="ainav.nz Home">
      <svg class="side-logo" viewBox="0 0 46 40" fill="none">
        <ellipse cx="18" cy="25" rx="12" ry="11" fill="#003B4F"/>
        <ellipse cx="15" cy="16" rx="9" ry="8" fill="#003B4F"/>
        <path d="M11 22 C10 18 12 12 16 10 C17 10 17 12 16 14 C14 17 12 20 12 23Z" fill="#003B4F"/>
        <path d="M20 12 C25 8 31 5.5 35 5 C36.5 4.8 37 6 35.5 6.5 C33 7.5 27 9.5 23 13Z" fill="#D4A843"/>
        <circle cx="17" cy="12" r="2" fill="white"/>
        <circle cx="17.5" cy="12" r="1" fill="#003B4F"/>
        <line x1="21" y1="14" x2="26" y2="14.5" stroke="#003B4F" stroke-width="0.7" opacity="0.6"/>
        <line x1="21" y1="15.5" x2="27" y2="16" stroke="#003B4F" stroke-width="0.7" opacity="0.6"/>
        <line x1="21" y1="17" x2="26" y2="17.5" stroke="#003B4F" stroke-width="0.7" opacity="0.6"/>
        <path d="M12 36 L11 40 M17 36 L17 40 M22 36 L23 40" stroke="#003B4F" stroke-width="1.8" stroke-linecap="round"/>
      </svg>
      <div><span class="side-name">ainav.nz</span><span class="side-tag">NZ AI Navigator</span></div>
    </a>
  </div>'''

# Pattern to match any wrong side-head (emoji logo or wrong SVG)
# Matches <div class="side-head">...</div> where the content is NOT the correct SVG
pattern = r'<div class="side-head">\s*<a class="side-brand"[^>]*>.*?</a>\s*</div>'

files = [
    r"D:\ainav-nz-pages\net-to-gross.html",
    r"D:\ainav-nz-pages\lump-sum-tax.html",
    r"D:\ainav-nz-pages\mortgage-refix-savings.html",
]

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()

    # Check if already correct (contains ellipse which is unique to correct SVG)
    if '<ellipse cx="18"' in content:
        print(f"  Already correct: {os.path.basename(f)}")
        continue

    # Replace the entire side-head section
    new_content = re.sub(pattern, correct_sidehead, content, flags=re.DOTALL)

    if new_content != content:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(new_content)
        print(f"  Fixed: {os.path.basename(f)}")
    else:
        print(f"  WARNING: Could not match side-head in {os.path.basename(f)}")

print("Done.")
