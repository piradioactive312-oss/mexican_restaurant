import glob

html_files = glob.glob('*.html')
replacement = """    <link rel="stylesheet" type="text/css" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/regular/style.css">
    <link rel="stylesheet" type="text/css" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/bold/style.css">
    <link rel="stylesheet" type="text/css" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/fill/style.css">"""

for f in html_files:
    content = open(f, encoding='utf-8').read()
    content = content.replace('<script src="https://unpkg.com/@phosphor-icons/web"></script>', replacement)
    open(f, 'w', encoding='utf-8').write(content)
