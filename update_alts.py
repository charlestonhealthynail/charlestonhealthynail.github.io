import os
import glob

directory = "/Users/thaophuong/Downloads/royal-nail"
html_files = glob.glob(os.path.join(directory, "*.html"))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    content = content.replace('alt="Nail Art"', 'alt="Nail Art - Charleston Healthy Nail"')
    content = content.replace('alt="Nail Design"', 'alt="Nail Design - Charleston Healthy Nail"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Alt tags updated for SEO.")
