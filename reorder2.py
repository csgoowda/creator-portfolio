import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

handmade_start = html.find('<!-- Handmade Art Section -->')
handmade_end = html.find('<!-- Bento Arsenal Grid -->')
handmade_sec = html[handmade_start:handmade_end]

# remove it from original location
html = html[:handmade_start] + html[handmade_end:]

# find insertion point after Web Dev
web_dev_start = html.find('<!-- Custom Website Development Section -->')
web_dev_end = html.find('<!-- Restaurant & Cafe Social Media Growth Section -->', web_dev_start)

# insert
new_html = html[:web_dev_end] + handmade_sec + html[web_dev_end:]

# Now let's redesign the handmade section's images
# I will use regex because exact spacing might differ.
old_gallery_pattern = r'<!-- Premium Gallery Alignment -->.*?</div>\s*</div>\s*<div style="margin-top: 1rem; text-align: center; width: 100%;">'

new_gallery = '''<!-- Dynamic Masonry-Style Gallery Alignment -->
          <div class="handmade-gallery-wrapper" style="margin-top: 3rem; width: 100%; max-width: 1100px;">
            <div class="handmade-icons masonry-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem; align-items: start;">
              
              <!-- Image 1 -->
              <div class="gallery-card magnetic" data-strength="15" style="position: relative; border-radius: 24px; overflow: hidden; padding-bottom: 110%; box-shadow: var(--shadow-lg); border: 1px solid rgba(255,255,255,0.1);">
                <img src="hand1.png" alt="Heart Icon" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; transition: transform 0.8s var(--ease);" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'" />
                <div style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.6) 0%, transparent 40%); pointer-events: none;"></div>
                <div style="position: absolute; bottom: 20px; left: 20px; color: white;">
                  <h4 style="margin:0; font-size: 1.3rem; text-shadow: 0 2px 10px rgba(0,0,0,0.5);">Handmade Hearts</h4>
                </div>
              </div>
              
              <!-- Image 2 (Featured shifted) -->
              <div class="gallery-card featured-card magnetic" data-strength="15" style="position: relative; border-radius: 24px; overflow: hidden; padding-bottom: 130%; box-shadow: var(--shadow-xl); border: 1px solid rgba(255,255,255,0.2);">
                <img src="hand2.png" alt="Brush Icon" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; transition: transform 0.8s var(--ease);" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'" />
                <div style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.6) 0%, transparent 40%); pointer-events: none;"></div>
                <div style="position: absolute; bottom: 20px; left: 20px; color: white;">
                  <h4 style="margin:0; font-size: 1.3rem; text-shadow: 0 2px 10px rgba(0,0,0,0.5);">Custom Portraits</h4>
                </div>
              </div>
              
              <!-- Image 3 -->
              <div class="gallery-card magnetic" data-strength="15" style="position: relative; border-radius: 24px; overflow: hidden; padding-bottom: 110%; box-shadow: var(--shadow-lg); border: 1px solid rgba(255,255,255,0.1);">
                <img src="hand3.png" alt="Gift Icon" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; transition: transform 0.8s var(--ease);" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'" />
                <div style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.6) 0%, transparent 40%); pointer-events: none;"></div>
                <div style="position: absolute; bottom: 20px; left: 20px; color: white;">
                  <h4 style="margin:0; font-size: 1.3rem; text-shadow: 0 2px 10px rgba(0,0,0,0.5);">Premium Boxes</h4>
                </div>
              </div>

            </div>
          </div>
          <div style="margin-top: 3rem; text-align: center; width: 100%;">'''

new_html = re.sub(old_gallery_pattern, new_gallery, new_html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

css_append = '''
/* Masonry Gallery Custom CSS */
@media (min-width: 769px) {
  .featured-card {
    transform: translateY(40px);
  }
}
@media (max-width: 768px) {
  .featured-card {
    transform: translateY(0);
  }
  .handmade-gallery-wrapper {
      margin-top: 1rem !important;
  }
}
'''
with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_append)
print("Updated Layout")
