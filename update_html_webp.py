import glob

html_files = glob.glob('*.html')
for f in html_files:
    content = open(f, encoding='utf-8').read()
    # Replace pngs with webp for the 5 optimized files
    for name in ['menu-drinks', 'menu-main-dishes', 'menu-sandwiches', 'menu-side-dishes', 'menu-starters']:
        content = content.replace(f'{name}.png', f'{name}.webp')
    open(f, 'w', encoding='utf-8').write(content)
