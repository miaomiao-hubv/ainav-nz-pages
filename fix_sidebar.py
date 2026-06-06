import os

correct_svg = '''      <svg class="side-logo" viewBox="0 0 46 40" fill="none">
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
      </svg>'''

wrong_svg = '''      <svg class="side-logo" viewBox="0 0 46 40" fill="none">
        <rect x="2" y="2" width="42" height="36" rx="8" fill="#003B4F"/>
        <text x="23" y="26" text-anchor="middle" font-size="18" font-weight="800" fill="#5EEAD4" font-family="system-ui">NZ</text>
        <path d="M8 34 L38 34 L38 37 L8 37Z" fill="#003B4F" opacity="0.3"/>
      </svg>'''

emoji_logo = '      <div class="side-logo">🧭</div>'

files = [
    r"D:\ainav-nz-pages\net-to-gross.html",
    r"D:\ainav-nz-pages\lump-sum-tax.html",
    r"D:\ainav-nz-pages\mortgage-refix-savings.html",
]

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()

    modified = False

    if wrong_svg in content:
        content = content.replace(wrong_svg, correct_svg)
        modified = True
        print(f"  Fixed wrong SVG: {os.path.basename(f)}")

    if emoji_logo in content:
        content = content.replace(emoji_logo, correct_svg)
        modified = True
        print(f"  Fixed emoji logo: {os.path.basename(f)}")

    # Fix side-name/tag
    old_branding = '<div class="side-name">NZ Local Toolkit</div><div class="side-tag">ainav.nz • All Tools</div>'
    new_branding = '<div><span class="side-name">ainav.nz</span><span class="side-tag">NZ AI Navigator</span></div>'
    if old_branding in content:
        content = content.replace(old_branding, new_branding)
        modified = True
        print(f"  Fixed branding text: {os.path.basename(f)}")

    if modified:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(content)
        print(f"  Saved: {os.path.basename(f)}")
    else:
        print(f"  No change: {os.path.basename(f)}")

print("All done.")
