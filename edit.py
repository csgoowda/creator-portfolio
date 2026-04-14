import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove Culinary Excellence
# Using the exact HTML comment blocks wrapping the section
start_marker = '<!-- Restaurant & Cafe Social Media Growth Section -->'
end_marker = '<!-- Dynamic Arsenal-Themed Video Accordion -->'
start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx != -1 and end_idx != -1:
    html = html[:start_idx] + html[end_idx:]
else:
    print("Could not find Culinary markers")

# 2. Fix Hero Title
html = re.sub(
    r'<h1 class="hero-title fade-up stagger-2">\s*Creative Digital Services &amp; <br>\s*<span class="gradient-text type-effect">Handmade Creations</span>\s*</h1>',
    '<h1 class="hero-title fade-up stagger-2" style="font-size: clamp(2.5rem, 6vw, 4.5rem);">Creative Digital Services &amp; <span class="gradient-text type-effect">HandmadeCreations</span></h1>',
    html
)
html = re.sub(
    r'<h1 class="hero-title fade-up stagger-2">\s*Creative Digital Services &amp;\s*<span class="gradient-text type-effect">Handmade\s*Creations</span>\s*</h1>',
    '<h1 class="hero-title fade-up stagger-2" style="font-size: clamp(2.5rem, 6vw, 4.5rem);">Creative Digital Services &amp; <span class="gradient-text type-effect">HandmadeCreations</span></h1>',
    html
)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Done")
