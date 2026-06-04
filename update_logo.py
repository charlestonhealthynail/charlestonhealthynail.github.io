import os
import glob

directory = "/Users/thaophuong/Downloads/royal-nail"
html_files = glob.glob(os.path.join(directory, "*.html"))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    content = content.replace('logo.jpg', 'logo.png')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Logo updated to logo.png in all HTML files.")
