import os
import glob

directory = "/Users/thaophuong/Downloads/royal-nail"
html_files = glob.glob(os.path.join(directory, "*.html"))

replacements = {
    "Fora Nail Lashes Spa": "Charleston Healthy Nail",
    "Fora": "Charleston Healthy Nail", # Note: need to be careful with this if it replaces "Fora" in unexpected places. Let's do exact matches first.
    "11455 E Carson St C&D, Lakewood, CA 90715": "1220 Ben Sawyer Blvd Suite S, Mt Pleasant, SC 29464",
    "Lakewood, CA 90715": "Mt Pleasant, SC 29464",
    "(562) 924-7078": "(854) 227-5153",
    "5629247078": "8542275153",
    "https://foranailslashesspa3332.simplepos.us/": "#",
    "nail salon lakewood": "nail salon mt-pleasant",
    "manicures lakewood": "manicures mt-pleasant",
    "pedicures lakewood": "pedicures mt-pleasant",
    "beauty salon 90715": "beauty salon 29464",
    "LAKEWOOD, CALIFORNIA": "MT PLEASANT, SOUTH CAROLINA",
    "BEST NAIL SALON IN LAKEWOOD": "BEST NAIL SALON IN MT PLEASANT",
    "nail salon in Lakewood": "nail salon in Mt Pleasant",
    "relaxation in Lakewood": "relaxation in Mt Pleasant",
    "fora+nail+lashes+spa+lakewood": "charleston+healthy+nail+mt+pleasant",
    "Lakewood": "Mt Pleasant",
    "LAKEWOOD": "MT PLEASANT",
    "lakewood": "mt-pleasant",
}

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Do replacements carefully to avoid double replacement.
    # We will do them in the order of the dict keys.
    # Actually wait, Fora is a substring of Fora Nail Lashes Spa.
    # So we should replace the longer string first.
    # Let's redefine replacements as an ordered list of tuples.
    rep_list = [
        ("Fora Nail Lashes Spa", "Charleston Healthy Nail"),
        ("Fora", "Charleston Healthy Nail"),
        ("11455 E Carson St C&D, Lakewood, CA 90715", "1220 Ben Sawyer Blvd Suite S, Mt Pleasant, SC 29464"),
        ("11455 E Carson St C&D", "1220 Ben Sawyer Blvd Suite S"),
        ("(562) 924-7078", "(854) 227-5153"),
        ("5629247078", "8542275153"),
        ("https://foranailslashesspa3332.simplepos.us/", "#"),
        ("nail salon lakewood", "nail salon mt-pleasant"),
        ("manicures lakewood", "manicures mt-pleasant"),
        ("pedicures lakewood", "pedicures mt-pleasant"),
        ("beauty salon 90715", "beauty salon 29464"),
        ("LAKEWOOD, CALIFORNIA", "MT PLEASANT, SOUTH CAROLINA"),
        ("BEST NAIL SALON IN LAKEWOOD", "BEST NAIL SALON IN MT PLEASANT"),
        ("nail salon in Lakewood", "nail salon in Mt Pleasant"),
        ("relaxation in Lakewood", "relaxation in Mt Pleasant"),
        ("fora+nail+lashes+spa+lakewood", "charleston+healthy+nail+mt+pleasant"),
        ("Lakewood, CA 90715", "Mt Pleasant, SC 29464"),
        ("Lakewood", "Mt Pleasant"),
        ("LAKEWOOD", "MT PLEASANT"),
        ("lakewood", "mt-pleasant"),
        ("90715", "29464")
    ]
    
    for old, new in rep_list:
        content = content.replace(old, new)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Replacements completed.")
