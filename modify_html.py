import re

with open('/Users/eliaskotsias/Desktop/Seaside Photos/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Bubble
text = text.replace('    .reveal.visible {\n      opacity: 1;\n      transform: translateY(0)\n    }\n  </style>', '''    .reveal.visible {
      opacity: 1;
      transform: translateY(0)
    }

    .discount-bubble {
      position: fixed;
      bottom: 24px;
      left: 24px;
      z-index: 9999;
      background: linear-gradient(135deg, #c9a55a, #a68442);
      color: white;
      padding: 14px 24px;
      border-radius: 50px;
      font-family: 'Jost', sans-serif;
      font-weight: 600;
      font-size: 14px;
      letter-spacing: 0.5px;
      box-shadow: 0 10px 25px rgba(201, 165, 90, 0.4);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 10px;
      transition: all 0.3s ease;
      animation: floatBubble 3s ease-in-out infinite;
    }
    .discount-bubble:hover {
      transform: translateY(-3px) scale(1.02);
      box-shadow: 0 15px 30px rgba(201, 165, 90, 0.5);
    }
    @keyframes floatBubble {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-8px); }
    }
    @media (max-width: 768px) {
      .discount-bubble {
        bottom: 80px; 
        left: 50%;
        transform: translateX(-50%);
        padding: 12px 20px;
        font-size: 13px;
        white-space: nowrap;
        animation: floatBubbleMobile 3s ease-in-out infinite;
      }
      .discount-bubble:hover {
        transform: translateX(-50%) translateY(-3px);
      }
      @keyframes floatBubbleMobile {
        0%, 100% { transform: translateX(-50%) translateY(0); }
        50% { transform: translateX(-50%) translateY(-8px); }
      }
    }
  </style>''')

text = text.replace('<div class="toast" id="toast"></div>', '''<div class="toast" id="toast"></div>

  <div class="discount-bubble reveal" onclick="openDirectModal('Seaside Luxury Apartment')">
    <span style="font-size: 18px;">🎁</span> <span data-i18n="nav-discount">15% Off - Book Direct!</span>
  </div>''')

# 2. Hero Widget Room Type Select Remove
text = re.sub(r'<div class="widget-field"><label data-i18n="lbl-room">Room Type</label>.*?</div>\s*<button class="widget-btn"', '<button class="widget-btn"', text, flags=re.DOTALL)

# 3. Rooms grid, replacing all rooms with 1 room, with no price
rooms_grid_replacement = """<div class="rooms-grid">
      <div class="room-card reveal" style="max-width: 800px; margin: 0 auto;" onclick="openDirectModal('Seaside Luxury Apartment')">
        <div class="room-img-wrap"><img class="room-img" src="343548430.jpg" alt="Seaside Luxury Apartment">
          <div class="room-tag" style="background:var(--navy);color:white" data-i18n="tag-pop">Most Popular</div>
        </div>
        <div class="room-info">
          <div class="room-name" data-i18n="room-1">Seaside Luxury Apartment</div>
          <p class="room-desc" data-i18n="r1-desc">Our signature apartment features panoramic Aegean views, a spacious layout, and a private terrace where the sea breeze greets you each morning. Impeccably furnished for your comfort.</p>
          <div class="room-feats">
            <span class="feat-tag" data-i18n="f-2g">2-4 Guests</span><span class="feat-tag" data-i18n="f-sea">Sea View</span><span class="feat-tag" data-i18n="f-ter">Private Terrace</span><span class="feat-tag" data-i18n="f-kitch">Full Kitchen</span><span class="feat-tag" data-i18n="f-show">Walk-in Shower</span>
          </div>
          <div class="room-footer" style="flex-direction: row; justify-content: flex-end;">
            <button class="btn-book" style="width: auto; padding: 14px 24px;"><span data-i18n="btn-book">Book Accommodation</span><span class="btn-arrow"><svg
                  viewBox="0 0 16 19" xmlns="http://www.w3.org/2000/svg">
                  <path
                    d="M7 18C7 18.5523 7.44772 19 8 19C8.55228 19 9 18.5523 9 18H7ZM8.70711 0.292893C8.31658 -0.0976311 7.68342 -0.0976311 7.29289 0.292893L0.928932 6.65685C0.538408 7.04738 0.538408 7.68054 0.928932 8.07107C1.31946 8.46159 1.95262 8.46159 2.34315 8.07107L8 2.41421L13.6569 8.07107C14.0474 8.46159 14.6805 8.46159 15.0711 8.07107C15.4616 7.68054 15.4616 7.04738 15.0711 6.65685L8.70711 0.292893ZM9 18L9 1H7L7 18H9Z">
                  </path>
                </svg></span></button>
          </div>
        </div>
      </div>
    </div>"""
text = re.sub(r'<div class="rooms-grid">.*?</div>\s*</section>', rooms_grid_replacement + '\n  </section>', text, flags=re.DOTALL)

# 4. Remove cal-tabs
text = re.sub(r'<div class="calendar-tabs reveal" id="cal-tabs">.*?</div>\s*<div class="calendar-container reveal">', '<div class="calendar-container reveal">', text, flags=re.DOTALL)

# 5. Remove footer room links
text = re.sub(r'<h4 data-i18n="foot-r1">Rooms</h4>\s*<ul>.*?</ul>', '<h4 data-i18n="foot-r1">Accommodation</h4>\n        <ul>\n          <li><a href="#rooms" data-i18n="room-1">Seaside Luxury Apartment</a></li>\n        </ul>', text, flags=re.DOTALL)

# 6. Change direct-modal text to emphasize discount
modal_desc_replacement = '<p class="modal-pitch" data-i18n="mod-desc"><b>Claim your 15% discount!</b> Booking platforms charge high hidden fees. Contact us directly on your preferred platform to secure your dates at an exclusive discounted rate!</p>'
text = re.sub(r'<p class="modal-pitch" data-i18n="mod-desc">.*?</p>', modal_desc_replacement, text, flags=re.DOTALL)

# 7. Javascript - ROOM_PRICES and roomsAvailability
text = text.replace("const ROOM_PRICES = { 'Studio Apartment': 85, 'Sea View Suite': 120, 'Deluxe Family Apartment': 155 };", "const ROOM_PRICES = { 'Seaside Luxury Apartment': 120 };")

text = text.replace("""    const roomsAvailability = {
      'Studio Apartment': generateMockBookings(0.3),
      'Sea View Suite': generateMockBookings(0.6),
      'Deluxe Family Apartment': generateMockBookings(0.4)
    };

    let currentCalDate = new Date();
    let currentCalRoom = 'Studio Apartment';""", """    const roomsAvailability = {
      'Seaside Luxury Apartment': generateMockBookings(0.4)
    };

    let currentCalDate = new Date();
    let currentCalRoom = 'Seaside Luxury Apartment';""")

# Update quickBook logic where it changes room tabs
text = re.sub(r'const rt = document\.getElementById\(\'room-type\'\)\.value;\n\n      if \(\!ci \|\| \!co\) \{', 'if (!ci || !co) {', text)
text = re.sub(r'if \(rt && rt !== \'\'\) \{.*?\}', '', text, flags=re.DOTALL)
text = text.replace("let optVal = currentCalRoom === 'Deluxe Family' ? 'Deluxe Family Apartment' : currentCalRoom;", "let optVal = 'Seaside Luxury Apartment';")

# Translations english (room-1, room-2, etc)
text = text.replace('"room-1": "Studio Apartment", "r1-desc": "A beautifully appointed open-plan studio with full kitchen facilities, ideal for couples seeking a romantic coastal retreat.",', '"room-1": "Seaside Luxury Apartment", "r1-desc": "Our signature apartment features panoramic Aegean views, a spacious layout, and a private terrace where the sea breeze greets you each morning. Impeccably furnished for your comfort.",\n        "nav-discount": "15% Off - Book Direct!",')
text = text.replace('"mod-title": "Unlock Direct Pricing", "mod-desc": "Booking platforms charge high hidden fees. Contact us directly on your preferred platform to secure your dates at a special discounted rate!"', '"mod-title": "Unlock Direct Pricing", "mod-desc": "<b>Claim your 15% discount!</b> Booking platforms charge high hidden fees. Contact us directly on your preferred platform to secure your dates at an exclusive discounted rate!"')

with open('/Users/eliaskotsias/Desktop/Seaside Photos/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("HTML and JS modified successfully!")
