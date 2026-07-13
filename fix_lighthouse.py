import os
import urllib.request
import glob

# Ensure directories exist
base_dir = 'C:\\Users\\Pedro\\.gemini\\antigravity\\scratch\\authentic-mexican-flavors'
phosphor_dir = os.path.join(base_dir, 'assets', 'css', 'phosphor')
os.makedirs(phosphor_dir, exist_ok=True)

# Files to download
weights = ['regular', 'bold', 'fill']
base_url = 'https://unpkg.com/@phosphor-icons/web@2.1.1/src/'

fonts_mapping = {
    'regular': 'Phosphor.woff2',
    'bold': 'Phosphor-Bold.woff2',
    'fill': 'Phosphor-Fill.woff2'
}

for weight in weights:
    # Download CSS
    css_url = f"{base_url}{weight}/style.css"
    css_path = os.path.join(phosphor_dir, f"{weight}.css")
    req = urllib.request.Request(css_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        css_content = response.read().decode('utf-8')
    
    # Change font-display to swap
    css_content = css_content.replace('font-display: block;', 'font-display: swap;')
    css_content = css_content.replace('font-display:block;', 'font-display: swap;')
    
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_content)
        
    # Download WOFF2
    font_file = fonts_mapping[weight]
    font_url = f"{base_url}{weight}/{font_file}"
    font_path = os.path.join(phosphor_dir, font_file)
    req = urllib.request.Request(font_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        with open(font_path, 'wb') as f:
            f.write(response.read())

print("Phosphor downloaded and patched.")

# Update HTML files
html_files = glob.glob(os.path.join(base_dir, '*.html'))
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Update phosphor links
    content = content.replace(
        '<link rel="stylesheet" type="text/css" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/regular/style.css">',
        '<link rel="stylesheet" href="assets/css/phosphor/regular.css">'
    )
    content = content.replace(
        '<link rel="stylesheet" type="text/css" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/bold/style.css">',
        '<link rel="stylesheet" href="assets/css/phosphor/bold.css">'
    )
    content = content.replace(
        '<link rel="stylesheet" type="text/css" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/fill/style.css">',
        '<link rel="stylesheet" href="assets/css/phosphor/fill.css">'
    )
    
    # 2. Add aria-label to menu-btn
    content = content.replace(
        '<button id="menu-btn" class="md:hidden text-white text-3xl focus:outline-none z-50">',
        '<button id="menu-btn" aria-label="Toggle mobile menu" class="md:hidden text-white text-3xl focus:outline-none z-50">'
    )
    
    # 3. Add defer to tailwind script
    content = content.replace(
        '<script src="https://cdn.tailwindcss.com"></script>',
        '<script defer src="https://cdn.tailwindcss.com"></script>'
    )
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("HTML files updated.")
