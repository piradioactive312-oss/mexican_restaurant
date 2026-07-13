import glob

for f in glob.glob('*.html'):
    content = open(f, encoding='utf-8').read()
    new_content = content.replace('<footer class="bg-mex-green ', '<footer class="bg-mex-green rounded-t-[3rem] ')
    open(f, 'w', encoding='utf-8').write(new_content)
