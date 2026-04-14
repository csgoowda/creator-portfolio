import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Instead of complex regex which might fail, let's use string splitting on known comment boundaries or section tags, since the HTML is nicely formatted with comments.

# Boundaries
head_end = html.find('<!-- Navigation -->')
nav_end = html.find('<!-- Hero Section -->')
hero_end = html.find('<!-- Infinite Stack Marquee -->')
marquee_end = html.find('<!-- Bento Arsenal Grid -->')
arsenal_end = html.find('<!-- Dynamic Arsenal-Themed Video Accordion -->')
work_end = html.find('<!-- Restaurant & Cafe Social Media Growth Section -->')
restaurant_end = html.find('<!-- Custom Website Development Section -->')
webdev_end = html.find('<!-- Handmade Art Section -->')
handmade_end = html.find('<!-- Contact & Footer -->')
contact_end = html.find('</main>')

# Extract sections
head_to_nav = html[:hero_end]
hero_section = html[hero_end:marquee_end] # wait, no, the indices above indicate the start of the section.

def get_section(start_marker, end_marker):
    start = html.find(start_marker)
    if end_marker:
        end = html.find(end_marker)
        return html[start:end]
    else:
        return html[start:]

# Fix definitions
nav_sec = html[:html.find('<!-- Hero Section -->')]
hero_sec = get_section('<!-- Hero Section -->', '<!-- Infinite Stack Marquee -->')
marquee_sec = get_section('<!-- Infinite Stack Marquee -->', '<!-- Bento Arsenal Grid -->')
arsenal_sec = get_section('<!-- Bento Arsenal Grid -->', '<!-- Dynamic Arsenal-Themed Video Accordion -->')
work_sec = get_section('<!-- Dynamic Arsenal-Themed Video Accordion -->', '<!-- Restaurant & Cafe Social Media Growth Section -->')
restaurant_sec = get_section('<!-- Restaurant & Cafe Social Media Growth Section -->', '<!-- Custom Website Development Section -->')
webdev_sec = get_section('<!-- Custom Website Development Section -->', '<!-- Handmade Art Section -->')
handmade_sec = get_section('<!-- Handmade Art Section -->', '<!-- Contact & Footer -->')
contact_and_footer = get_section('<!-- Contact & Footer -->', None)

# 1. Update logo & nav links in nav_sec
nav_sec = nav_sec.replace('CHETHAN<span class="dot">.</span>', 'CS GOWDA<span class="dot">.</span>')
nav_sec = nav_sec.replace('<a href="#expertise" class="magnetic" data-strength="20">Expertise</a>', '<a href="#main-services" class="magnetic" data-strength="20">Services</a>')
nav_sec = nav_sec.replace('<a href="#web-dev" class="magnetic" data-strength="20">Services</a>', '<a href="#expertise" class="magnetic" data-strength="20">Arsenal</a>')
nav_sec = nav_sec.replace('<a href="#work" class="magnetic" data-strength="20">Work</a>', '<a href="#work" class="magnetic" data-strength="20">Portfolio</a>')
nav_sec = nav_sec.replace('<a href="#handmade" class="magnetic" data-strength="20">Handmade</a>', '<a href="#handmade" class="magnetic" data-strength="20">Handmade Gifts</a>')
nav_sec = nav_sec.replace('<a href="#contact" class="btn btn-outline magnetic" data-strength="30">Let\'s Talk</a>', '<a href="#contact" class="btn btn-outline magnetic" data-strength="30">Contact Now</a>')

# 2. Update Hero
hero_replacement = """
    <!-- Hero Section -->
    <section class="hero" id="home">
      <div class="container hero-container">

        <div class="hero-content reveal">
          <div class="hero-badge fade-up stagger-1">Creator Portfolio</div>
          <h1 class="hero-title fade-up stagger-2">
            Creative Digital Services &amp; <br>
            <span class="gradient-text type-effect">Handmade Creations</span>
          </h1>
          <p class="hero-subtitle fade-up stagger-3">
            Web Development | Social Media Management | Handmade Gifts<br>
            Transforming your brand with professional digital solutions and unique personalized creations.
          </p>
          <div class="hero-cta fade-up stagger-4">
            <a href="#main-services" class="btn btn-solid magnetic" data-strength="40">View Services</a>
            <a href="#contact" class="btn btn-ghost link-hover magnetic" data-strength="20">Contact Now ↗</a>
          </div>
        </div>
"""
hero_sec = re.sub(r'<!-- Hero Section -->.*?</div>\s*</div>', hero_replacement, hero_sec, flags=re.DOTALL, count=1)

# 3. Create Main Services Section
main_services_sec = """
    <!-- Main Services Section -->
    <section class="main-services-section" id="main-services">
      <div class="container">
        <div class="arsenal-header fade-up" style="margin-bottom: 3rem; text-align: center;">
          <div class="arsenal-badge">OUR SERVICES</div>
          <h2 class="section-title">Core <span class="gradient-text">Offerings</span></h2>
        </div>

        <div class="arsenal-bento" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
          <!-- Card 1 -->
          <div class="bento-card fade-up" style="--d: 0.1s">
            <div class="card-glass"></div>
            <div class="card-content" style="align-items: center; text-align: center; justify-content: center;">
              <div class="card-icon" style="margin: 0 auto 1.5rem auto;">
                <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2">
                  <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
                  <line x1="8" y1="21" x2="16" y2="21"></line>
                  <line x1="12" y1="17" x2="12" y2="21"></line>
                </svg>
              </div>
              <div class="card-text">
                <h3 style="font-size: 1.5rem;">Website Development</h3>
                <p style="margin-top: 1rem;">Professional websites for business, portfolio, and personal branding.</p>
              </div>
            </div>
          </div>

          <!-- Card 2 -->
          <div class="bento-card fade-up" style="--d: 0.2s">
            <div class="card-glass"></div>
            <div class="card-content" style="align-items: center; text-align: center; justify-content: center;">
              <div class="card-icon" style="margin: 0 auto 1.5rem auto;">
                <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2">
                  <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path>
                </svg>
              </div>
              <div class="card-text">
                <h3 style="font-size: 1.5rem;">Social Media Management</h3>
                <p style="margin-top: 1rem;">Grow your Instagram and online presence with professional management.</p>
              </div>
            </div>
          </div>

          <!-- Card 3 -->
          <div class="bento-card fade-up" style="--d: 0.3s">
            <div class="card-glass"></div>
            <div class="card-content" style="align-items: center; text-align: center; justify-content: center;">
              <div class="card-icon" style="margin: 0 auto 1.5rem auto;">
                <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2">
                  <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
                </svg>
              </div>
              <div class="card-text">
                <h3 style="font-size: 1.5rem;">Handmade Heart Gifts</h3>
                <p style="margin-top: 1rem;">Unique handmade heart designs and custom gifts for special occasions.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
"""

# Update arsenal (add intro)
arsenal_intro = """
        <div class="arsenal-header fade-up">
          <div class="arsenal-badge">ABOUT ME</div>
          <h2 class="section-title">My <span class="gradient-text">Arsenal</span></h2>
          <p class="hero-subtitle" style="margin-top: 1rem;">I am a creative developer and designer providing digital and handmade creative services.</p>
        </div>
"""
arsenal_sec = re.sub(r'<div class="arsenal-header fade-up">.*?</div>', arsenal_intro, arsenal_sec, flags=re.DOTALL)

# Update contact
contact_replacement = """
    <!-- Contact & Footer -->
    <section class="contact-section" id="contact">
      <div class="container fade-up">
        <h2 class="giant-text">Let's Connect.</h2>
        <div class="command-center-grid stagger-reveal">
          <a href="https://wa.me/918095406516" target="_blank" class="command-card magnetic" data-strength="15">
            <div class="card-header">
              <span class="status-dot"></span>
              <span class="card-id">CH-01</span>
            </div>
            <div class="card-body">
              <h3>Direct WhatsApp Line</h3>
              <p>Message me instantly for discussing your project.</p>
              <span class="contact-val">8095406516 ↗</span>
            </div>
            <div class="card-footer">
              <span class="tech-tag">FAST-TRACK</span>
            </div>
            <div class="card-scanner"></div>
          </a>
          
          <a href="tel:8095406516" class="command-card magnetic" data-strength="15">
            <div class="card-header">
              <span class="status-dot"></span>
              <span class="card-id">CH-02</span>
            </div>
            <div class="card-body">
              <h3>Call Now</h3>
              <p>Require immediate discussion? Tap to ring me.</p>
              <span class="contact-val">8095406516 ↗</span>
            </div>
            <div class="card-footer">
              <span class="tech-tag">PHONE</span>
            </div>
            <div class="card-scanner"></div>
          </a>

          <a href="https://www.instagram.com/chethan_gxwda_/" target="_blank" class="command-card magnetic"
            data-strength="15">
            <div class="card-header">
              <span class="status-dot"></span>
              <span class="card-id">CH-03</span>
            </div>
            <div class="card-body">
              <h3>Visual Arsenal</h3>
              <p>Follow my creativity and work on Instagram.</p>
              <span class="contact-val">@chethan_gxwda_ ↗</span>
            </div>
            <div class="card-footer">
              <span class="tech-tag">PORTFOLIO</span>
            </div>
            <div class="card-scanner"></div>
          </a>
        </div>
        
        <!-- QR Code Section -->
        <div class="qr-code-section fade-up" style="margin-top: 4rem; text-align: center; border: 1px dashed var(--accent); padding: 3rem; border-radius: 12px; background: rgba(59, 130, 246, 0.02);">
          <h3 style="font-size: 1.5rem; margin-bottom: 2rem;">Scan to Visit</h3>
          <div class="qr-wrapper" style="background: white; padding: 10px; display: inline-block; border-radius: 8px;">
            <img src="https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://csgoowda.github.io/creator-portfolio/" alt="QR Code" width="150" height="150">
          </div>
          <p style="margin-top: 1rem;">csgoowda.github.io/creator-portfolio/</p>
        </div>
      </div>
    </section>
"""
# careful with footer
footer_sec = contact_and_footer[contact_and_footer.find('</main>'):]
contact_sec = contact_replacement + footer_sec
contact_sec = contact_sec.replace('CHETHAN.', 'CS GOWDA.')

# Handame edits (add CTA button)
handmade_cta = """          </div>
          <div style="margin-top: 3rem; text-align: center;">
            <a href="#contact" class="btn btn-solid magnetic" data-strength="30">Place a Gift Order</a>
          </div>
        </div>"""
handmade_sec = handmade_sec.replace('          </div>\n\n        </div>', handmade_cta)


# Build the final ordered document
final_html = (
    nav_sec + "\n" +
    hero_sec + "\n" +
    marquee_sec + "\n" +
    main_services_sec + "\n" +
    webdev_sec + "\n" +
    restaurant_sec + "\n" +
    work_sec + "\n" +
    handmade_sec + "\n" +
    arsenal_sec + "\n" +
    contact_sec
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Done processing HTML!")
