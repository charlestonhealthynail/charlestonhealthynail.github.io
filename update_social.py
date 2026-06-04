import os
import glob
import re

directory = "/Users/thaophuong/Downloads/royal-nail"
html_files = glob.glob(os.path.join(directory, "*.html"))

social_html = """    <!-- Floating Social Tabs (Left) -->
    <div class="floating-social">
        <a href="#" target="_blank" class="social-tab" title="Yelp" aria-label="Yelp">
            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12.756 16.326c-.347-.291-.703-.312-1.077-.075l-4.524 2.88c-.378.237-.47.616-.29.986.994 2.11 2.87 3.518 5.166 3.842 1.472.203 2.921-.137 4.195-.916.32-.196.38-.553.18-.89l-2.483-5.385c-.173-.374-.82-.15-1.167-.442zm6.208-4.492h-5.91c-.42 0-.693.308-.82.72l-1.524 5.097c-.114.385.087.64.444.757 2.11.722 4.316.51 6.223-.746 1.258-.82 2.064-2.022 2.39-3.518.067-.323-.178-.602-.505-.623-2.34-.14-3.6-.665-6.298-.687v-1.01h6zm-9.352 1.942l-4.706 3.195c-.328.225-.765.17-.996-.135-.85-1.31-1.2-2.842-1.012-4.408.125-1.042.502-2.015 1.096-2.836.216-.302.66-.356 1.01-.157l4.98 2.825c.35.2.496.634.346 1.01-.167.424-.343.837-.718 1.506zm3.504-1.637c.362 0 .61-.266.69-.618l1.545-6.68c.08-.344-.12-.66-.46-.777C12.44 3.328 9.94 3.506 7.9 4.673c-.982.56-1.742 1.348-2.227 2.302-.172.338.01.764.364.912 2.307.96 4.664 1.83 7.006 2.68.35.127.72.155 1.07.155z"/></svg>
        </a>
        <a href="#" target="_blank" class="social-tab" title="Instagram" aria-label="Instagram">
            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
        </a>
    </div>"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update the CSS for mobile floating social
    # Find .floating-social { display: none; }
    old_css_1 = ".floating-social { display: none; }"
    new_css = """.floating-social {
                display: flex;
                top: auto;
                bottom: 20px;
                left: 20px;
                transform: none;
                flex-direction: row;
                gap: 12px;
                z-index: 10000;
            }
            .floating-social .social-tab {
                border-radius: 50%;
                border: 1px solid rgba(197,160,89,0.4);
                width: 44px;
                height: 44px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.5);
            }
            .floating-social .social-tab:hover {
                width: 44px;
            }"""
    if old_css_1 in content:
        content = content.replace(old_css_1, new_css)
    else:
        # Check if the block is empty in about.html etc and add it.
        pass

    # 2. Replace the HTML for floating-social
    # index.html has the block, others have <!-- Floating Social -->
    
    # regex to find the floating-social div and replace it
    pattern = re.compile(r'<!-- Floating Social Tabs \(Left\).*?</div>|<!-- Floating Social -->', re.DOTALL)
    content = pattern.sub(social_html, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated floating social buttons.")
