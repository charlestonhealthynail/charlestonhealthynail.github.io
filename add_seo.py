import os
import glob

directory = "/Users/thaophuong/Downloads/royal-nail"
html_files = glob.glob(os.path.join(directory, "*.html"))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if open graph is already there
    if 'property="og:title"' in content:
        continue
        
    filename = os.path.basename(filepath)
    title = "Charleston Healthy Nail"
    if filename == "about.html":
        title = "About Us | Charleston Healthy Nail"
    elif filename == "service.html":
        title = "Services | Charleston Healthy Nail"
    elif filename == "gallery.html":
        title = "Gallery | Charleston Healthy Nail"
    elif filename == "index.html":
        title = "Charleston Healthy Nail | Top Rated Nail Salon in Mt Pleasant, SC"

    description = "Charleston Healthy Nail in Mt Pleasant offers premium manicures, pedicures, acrylics, and more. Experience luxury nail care with our expert technicians."
    
    og_tags = f"""
    <!-- Open Graph SEO -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:image" content="logo.jpg">
    <meta property="og:type" content="website">
    <meta property="og:locale" content="en_US">
    
    <!-- Schema.org JSON-LD -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "NailSalon",
      "name": "Charleston Healthy Nail",
      "image": "logo.jpg",
      "@id": "",
      "url": "#",
      "telephone": "(854) 227-5153",
      "address": {{
        "@type": "PostalAddress",
        "streetAddress": "1220 Ben Sawyer Blvd Suite S",
        "addressLocality": "Mt Pleasant",
        "addressRegion": "SC",
        "postalCode": "29464",
        "addressCountry": "US"
      }},
      "openingHoursSpecification": [
        {{
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
          "opens": "09:00",
          "closes": "19:00"
        }},
        {{
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": "Saturday",
          "opens": "09:00",
          "closes": "18:00"
        }}
      ]
    }}
    </script>
"""
    
    content = content.replace("</head>", og_tags + "</head>")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("SEO tags added successfully.")
