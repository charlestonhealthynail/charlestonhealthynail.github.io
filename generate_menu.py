import re

new_menu_html = """
  <!-- ACRYLICS & DIPPING -->
  <section class="section">
    <div class="section-label"><span class="section-label-icon">✦</span><span class="section-label-text">Acrylics (Free Gel)</span></div>
    <div class="simple-grid">
      <div class="simple-item"><span class="simple-name">Full Set</span><span class="simple-price">$50+</span></div>
      <div class="simple-item"><span class="simple-name">Full Set W. Color Powder</span><span class="simple-price">$55+</span></div>
      <div class="simple-item"><span class="simple-name">Full Set Ombre</span><span class="simple-price">$60+</span></div>
      <div class="simple-item"><span class="simple-name">Full Set Pink & White</span><span class="simple-price">$60+</span></div>
      <div class="simple-item"><span class="simple-name">Full Set Toe</span><span class="simple-price">$50+</span></div>
      <div class="simple-item"><span class="simple-name">Fill Acrylics (Free Cut Down)</span><span class="simple-price">$45+</span></div>
      <div class="simple-item"><span class="simple-name">Fill Pink & White</span><span class="simple-price">$50+</span></div>
      <div class="simple-item"><span class="simple-name">Fill Toes</span><span class="simple-price">$40+</span></div>
    </div>
  </section>

  <section class="section">
    <div class="section-label"><span class="section-label-icon">✦</span><span class="section-label-text">Dipping Powder</span></div>
    <div class="simple-grid">
      <div class="simple-item"><span class="simple-name">Natural Nails Dipping</span><span class="simple-price">$40+</span></div>
      <div class="simple-item"><span class="simple-name">Pink & White Dipping</span><span class="simple-price">$50+</span></div>
      <div class="simple-item"><span class="simple-name">Ombre Dipping</span><span class="simple-price">$50+</span></div>
    </div>
  </section>

  <!-- GEL-X & HYBRID & HARD GEL -->
  <section class="section">
    <div class="section-label"><span class="section-label-icon">✦</span><span class="section-label-text">Gel-X / Hybrid Gel / Hard Gel</span></div>
    <div class="enhance-grid">
      <div class="enhance-card">
        <div class="enhance-name">Gel-X</div>
        <div class="enhance-rows">
          <div class="enhance-row"><span class="enhance-row-label">Full Set Gel-X</span><span class="enhance-row-price">$57+</span></div>
          <div class="enhance-row"><span class="enhance-row-label">Fill Gel-X</span><span class="enhance-row-price">$45+</span></div>
        </div>
      </div>
      <div class="enhance-card">
        <div class="enhance-name">Hybrid Gel</div>
        <div class="enhance-rows">
          <div class="enhance-row"><span class="enhance-row-label">Full Set</span><span class="enhance-row-price">$55+</span></div>
          <div class="enhance-row"><span class="enhance-row-label">Fill Hybrid Gel</span><span class="enhance-row-price">$45+</span></div>
        </div>
      </div>
      <div class="enhance-card">
        <div class="enhance-name">Hard Gel / Gel Builder</div>
        <div class="enhance-rows">
          <div class="enhance-row"><span class="enhance-row-label">Full Set</span><span class="enhance-row-price">$50+</span></div>
          <div class="enhance-row"><span class="enhance-row-label">Fill Hard Gel</span><span class="enhance-row-price">$45+</span></div>
        </div>
      </div>
    </div>
  </section>

  <!-- TAKE OFF -->
  <section class="section">
    <div class="section-label"><span class="section-label-icon">✦</span><span class="section-label-text">Take Off Services</span></div>
    <div class="simple-grid">
      <div class="simple-item"><span class="simple-name">Take Off With Services (Acrylic/Gel-X/Hybrid/Hard Gel)</span><span class="simple-price">$10</span></div>
      <div class="simple-item"><span class="simple-name">Take Off With Services (Dipping)</span><span class="simple-price">$8</span></div>
      <div class="simple-item"><span class="simple-name">Take Off Without Service (Acrylic/Gel-X/Hybrid/Hard Gel)</span><span class="simple-price">$15</span></div>
      <div class="simple-item"><span class="simple-name">Take Off Without Service (Dipping)</span><span class="simple-price">$10</span></div>
      <div class="simple-item"><span class="simple-name">Take Off Without Service (Gel Only)</span><span class="simple-price">$8</span></div>
    </div>
  </section>

  <!-- ADDITIONAL SERVICES -->
  <section class="section">
    <div class="section-label"><span class="section-label-icon">✦</span><span class="section-label-text">Additional Services</span></div>
    <div class="simple-grid">
      <div class="simple-item"><span class="simple-name">Polish Change Toes or Hands</span><span class="simple-price">$12</span></div>
      <div class="simple-item"><span class="simple-name">Change Color Gel Toes or Hands</span><span class="simple-price">$22</span></div>
      <div class="simple-item"><span class="simple-name">Change Color Gel Acrylic Nails</span><span class="simple-price">$25</span></div>
      <div class="simple-item"><span class="simple-name">Broken Nails</span><span class="simple-price">$5+</span></div>
      <div class="simple-item"><span class="simple-name">Nails Design</span><span class="simple-price">$6+</span></div>
      <div class="simple-item"><span class="simple-name">French Tip</span><span class="simple-price">$7+</span></div>
      <div class="simple-item"><span class="simple-name">Matte Top Coat</span><span class="simple-price">$5</span></div>
      <div class="simple-item"><span class="simple-name">Buffer Shine</span><span class="simple-price">$7</span></div>
      <div class="simple-item"><span class="simple-name">Extra Callus Treatment</span><span class="simple-price">$7</span></div>
      <div class="simple-item"><span class="simple-name">Extra Paraffin</span><span class="simple-price">$10</span></div>
      <div class="simple-item"><span class="simple-name">Collagen Treatment</span><span class="simple-price">$10</span></div>
      <div class="simple-item"><span class="simple-name">Cuticle Cleaning</span><span class="simple-price">$7</span></div>
    </div>
  </section>

  <!-- LASHES -->
  <section class="section">
    <div class="section-label"><span class="section-label-icon">✦</span><span class="section-label-text">Eyelashes Extensions</span></div>
    <p style="font-family:'Libre Baskerville', serif; font-style:italic; font-size:0.85rem; color:var(--muted); margin-bottom:15px;">Professionals, delivering beautiful lashes every time. Enhance the length, curl, fullness, and thickness of natural eyelashes.</p>
    <div class="enhance-grid">
      <div class="enhance-card">
        <div class="enhance-rows">
          <div class="enhance-row"><span class="enhance-row-label">Classic<br><span style="font-size:0.7rem; color:var(--green-light);">Most natural look, Individual hair extension</span></span><span class="enhance-row-price">$95</span></div>
          <div class="enhance-row"><span class="enhance-row-label">Hybrid<br><span style="font-size:0.7rem; color:var(--green-light);">Subtle Fullness, mix of classic and Volume</span></span><span class="enhance-row-price">$110</span></div>
          <div class="enhance-row"><span class="enhance-row-label">Volume<br><span style="font-size:0.7rem; color:var(--green-light);">Fluffy Fullness, mix of thick fullness classic and volume</span></span><span class="enhance-row-price">$115</span></div>
        </div>
      </div>
    </div>
  </section>

  <!-- WAXING -->
  <section class="section">
    <div class="section-label"><span class="section-label-icon">✦</span><span class="section-label-text">Waxing</span></div>
    <div class="simple-grid">
      <div class="simple-item"><span class="simple-name">Eyebrows Tint</span><span class="simple-price">$20</span></div>
      <div class="simple-item"><span class="simple-name">Eyebrows</span><span class="simple-price">$12</span></div>
      <div class="simple-item"><span class="simple-name">Up Lip</span><span class="simple-price">$6</span></div>
      <div class="simple-item"><span class="simple-name">Chin</span><span class="simple-price">$14</span></div>
      <div class="simple-item"><span class="simple-name">Sideburn</span><span class="simple-price">$15</span></div>
      <div class="simple-item"><span class="simple-name">Full Face</span><span class="simple-price">$35+</span></div>
      <div class="simple-item"><span class="simple-name">Under Arms</span><span class="simple-price">$15</span></div>
      <div class="simple-item"><span class="simple-name">Full Arms</span><span class="simple-price">$40+</span></div>
      <div class="simple-item"><span class="simple-name">Half Arms</span><span class="simple-price">$30+</span></div>
      <div class="simple-item"><span class="simple-name">Full Legs</span><span class="simple-price">$55+</span></div>
      <div class="simple-item"><span class="simple-name">Half Legs</span><span class="simple-price">$40+</span></div>
      <div class="simple-item"><span class="simple-name">Full Back</span><span class="simple-price">$45+</span></div>
      <div class="simple-item"><span class="simple-name">Chest</span><span class="simple-price">$45+</span></div>
      <div class="simple-item"><span class="simple-name">Bikini</span><span class="simple-price">$35+</span></div>
      <div class="simple-item"><span class="simple-name">Brazilian</span><span class="simple-price">$50+</span></div>
    </div>
  </section>

  <!-- FACIAL -->
  <section class="section">
    <div class="section-label"><span class="section-label-icon">✦</span><span class="section-label-text">Facial</span></div>
    <div class="facial-grid">
      <div class="facial-card">
        <div class="facial-top">
          <div><div class="facial-name">Basic Facial</div><div class="facial-duration">45 mins</div></div>
          <div class="facial-price">$60</div>
        </div>
        <div class="facial-tagline">Cleaning, Face Steam, skin analysis, light exfoliation massage, mask, moisturize, sunscreen</div>
      </div>
      <div class="facial-card">
        <div class="facial-top">
          <div><div class="facial-name">Hydration Facial</div><div class="facial-duration">60 mins</div></div>
          <div class="facial-price">$90</div>
        </div>
        <div class="facial-tagline">Deep cleaning, face steam, intensive exfoliation, help remove dead skin cells, blackhead, white head, face massage with vitamin C serum to brighten tone up your skin, hydrating mask and therapeutic hot stone head massage, moisturize, sunscreen</div>
      </div>
    </div>
  </section>

  <!-- MANICURES -->
  <section class="section">
    <div class="section-label"><span class="section-label-icon">✦</span><span class="section-label-text">Manicures</span></div>
    <div class="tier-stack">
      <div class="tier-card">
        <div>
          <div class="tier-name">M1. Classic Manicure</div>
          <div class="tier-desc">Nails Trimming, Shaping, Cuticle Cleaning, Therapeutic lotion massage, and Polish color</div>
        </div>
        <div class="tier-prices"><div class="price-row"><span class="price-val">$20</span></div></div>
      </div>
      <div class="tier-card">
        <div>
          <div class="tier-name">M2. Bella Manicure</div>
          <div class="tier-desc">Nails Trimming, Shaping, Cuticle Cleaning, 5 Mins Hot Oil & Lotion Massage, Cooling Gel, Hot towels wrap, and Polish color</div>
        </div>
        <div class="tier-prices"><div class="price-row"><span class="price-val">$28</span></div></div>
      </div>
      <div class="tier-card">
        <div>
          <div class="tier-name">M3. Deluxe Manicure</div>
          <div class="tier-desc">Nails Trimming, Shaping, Cuticle Cleaning, Paraffin Wax, 7 Mins Hot Oil & Lotion Massage, Cooling Gel, Hot towel wrap, and Polish color</div>
        </div>
        <div class="tier-prices"><div class="price-row"><span class="price-val">$38</span></div></div>
      </div>
      <div class="tier-card">
        <div>
          <div class="tier-name">M4. Organic Manicure</div>
          <div class="tier-desc">Sea salt soak (Detoxify & Deodorize), Nails Trimming, Shaping, Cuticle Cleaning, Organic Exfoliation, Collagen Glove, 10 min Hot Organic Lotion Massage & Organic Mask, Two Hot Towels wrap, and Polish Color</div>
        </div>
        <div class="tier-prices"><div class="price-row"><span class="price-val">$48</span></div></div>
      </div>
      <div class="tier-card">
        <div>
          <div class="tier-name">Gel Manicure</div>
          <div class="tier-desc">(Free Take Off)</div>
        </div>
        <div class="tier-prices"><div class="price-row"><span class="price-val">$35</span></div></div>
      </div>
    </div>
  </section>

  <!-- PEDICURES -->
  <section class="section">
    <div class="section-label"><span class="section-label-icon">✦</span><span class="section-label-text">Pedicures</span></div>
    <div class="tier-stack">
      <div class="tier-card">
        <div>
          <div class="tier-name">P1. Classic Pedicure</div>
          <div class="tier-desc">Nails trimming, shaping, cuticle cleaning, lotion massage, hot towel wrap, and polish color.</div>
        </div>
        <div class="tier-prices"><div class="price-row"><span class="price-val">$27</span></div></div>
      </div>
      <div class="tier-card">
        <div>
          <div class="tier-name">P2. Sugar Scrub Pedicure</div>
          <div class="tier-desc">Nails trimming, shaping, cuticle cleaning, lavender exfoliation, 5 mins hot oil & lotion massage, hot towel wrap, and polish color.</div>
        </div>
        <div class="tier-prices"><div class="price-row"><span class="price-val">$34</span></div></div>
      </div>
      <div class="tier-card">
        <div>
          <div class="tier-name">P3. Bella Pedicure</div>
          <div class="tier-desc">Nails trimming, shaping, cuticle cleaning, callus treatment, mango exfoliation, 8 mins hot oil & lotion massage, two hot towels wrap, and polish color.</div>
        </div>
        <div class="tier-prices"><div class="price-row"><span class="price-val">$42</span></div></div>
      </div>
      <div class="tier-card">
        <div>
          <div class="tier-name">P4. Deluxe Pedicure</div>
          <div class="tier-desc">Nails trimming, shaping, cuticle cleaning, callus treatment, honey coffee exfoliation, paraffin wax, 10 mins hot oil & lotion massage, cooling gel, two hot towels wrap, and polish color.</div>
        </div>
        <div class="tier-prices"><div class="price-row"><span class="price-val">$50</span></div></div>
      </div>
      <div class="tier-card">
        <div>
          <div class="tier-name">P5. Organic Pedicure</div>
          <div class="tier-desc">Nails trimming, shaping, cuticle cleaning, callus treatment, organic exfoliation, paraffin wax, 12 mins hot oil & organic lotion massage and organic mask, two hot towels wrap, and polish color.</div>
        </div>
        <div class="tier-prices"><div class="price-row"><span class="price-val">$60</span></div></div>
      </div>
      <div class="tier-card">
        <div>
          <div class="tier-name">P6. Royal Organic Pedicure</div>
          <div class="tier-desc">Nails trimming, shaping, cuticle cleaning, callus treatment, organic exfoliation, collagen glove, 15 mins hot stone & organic lotion massage, organic mask, two hot towels wrap, and polish color.</div>
        </div>
        <div class="tier-prices"><div class="price-row"><span class="price-val">$70</span></div></div>
      </div>
      <div class="tier-card">
        <div>
          <div class="tier-name">Extra Gel</div>
          <div class="tier-desc">($5 charge for take off gel if don't apply gel again)</div>
        </div>
        <div class="tier-prices"><div class="price-row"><span class="price-val">$15</span></div></div>
      </div>
    </div>
  </section>

  <!-- KIDS MENU -->
  <section class="section">
    <div class="section-label"><span class="section-label-icon">✦</span><span class="section-label-text">Kid's Menu</span></div>
    <div class="simple-grid">
      <div class="simple-item"><span class="simple-name">Kid Manicure</span><span class="simple-price">$12</span></div>
      <div class="simple-item"><span class="simple-name">Kid Pedicure</span><span class="simple-price">$20</span></div>
      <div class="simple-item"><span class="simple-name">Kid Combo</span><span class="simple-price">$30</span></div>
      <div class="simple-item"><span class="simple-name">Extra Gel</span><span class="simple-price">$10</span></div>
      <div class="simple-item"><span class="simple-name">Design</span><span class="simple-price">$5+</span></div>
    </div>
  </section>
"""

with open('/Users/thaophuong/Downloads/royal-nail/service.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace header FORA with Charleston Healthy Nail
content = content.replace('<div class="salon-name"><span>FORA</span></div>', '<div class="salon-name"><span>Charleston</span> Healthy Nail</div>')
content = content.replace('<div class="footer-name">FORA NAILS LASHES SPA</div>', '<div class="footer-name">CHARLESTON HEALTHY NAIL</div>')

# Find the start and end of the old menu to replace it
start_marker = "<!-- MANICURE & PEDICURE -->"
end_marker = "<!-- FOOTER -->"

pattern = re.compile(rf'{start_marker}.*?(?={end_marker})', re.DOTALL)
content = pattern.sub(new_menu_html + '\n\n  ', content)

with open('/Users/thaophuong/Downloads/royal-nail/service.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Menu updated successfully.")
