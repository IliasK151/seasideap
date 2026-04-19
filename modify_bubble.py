import re

with open('/Users/eliaskotsias/Desktop/Seaside Photos/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace CSS
css_pattern = r'\.discount-bubble\s*\{.*?@keyframes floatBubbleMobile\s*\{\s*0%,\s*100%\s*\{\s*transform:\s*translateX\(-50%\)\s*translateY\(0\);\s*\}\s*50%\s*\{\s*transform:\s*translateX\(-50%\)\s*translateY\(-8px\);\s*\}\s*\}\s*\}'
new_css = """.discount-bubble {
      position: fixed;
      bottom: 24px;
      left: 24px;
      z-index: 9999;
      background: rgba(13, 27, 42, 0.85);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid rgba(201, 165, 90, 0.4);
      color: white;
      padding: 8px 16px 8px 8px;
      border-radius: 50px;
      font-family: 'Jost', sans-serif;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3), 0 0 15px rgba(201, 165, 90, 0.15);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 12px;
      transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    .discount-bubble::before {
      content: '';
      position: absolute;
      top: -1px; left: -1px; right: -1px; bottom: -1px;
      border-radius: 50px;
      border: 1px solid #c9a55a;
      opacity: 0;
      animation: pulseBorder 2.5s infinite ease-out;
      pointer-events: none;
    }

    .discount-bubble:hover {
      transform: translateY(-5px) scale(1.03);
      box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4), 0 0 25px rgba(201, 165, 90, 0.4);
      border-color: rgba(201, 165, 90, 0.8);
    }
    
    .bubble-icon {
      background: linear-gradient(135deg, #c9a55a, #a68442);
      width: 38px;
      height: 38px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: inset 0 2px 4px rgba(255,255,255,0.3), 0 4px 10px rgba(0,0,0,0.2);
    }
    
    .bubble-icon svg {
      width: 18px;
      height: 18px;
      fill: none;
      stroke: white;
      stroke-width: 2.2;
    }

    .bubble-content {
      display: flex;
      flex-direction: column;
      line-height: 1.2;
      padding-right: 4px;
    }

    .bubble-offer {
      color: #c9a55a;
      font-weight: 700;
      font-size: 15px;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }
    
    .bubble-action {
      font-size: 11px;
      opacity: 0.8;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      margin-top: 2px;
    }

    @keyframes pulseBorder {
      0% { transform: scale(1); opacity: 0.8; }
      100% { transform: scale(1.08, 1.15); opacity: 0; }
    }

    @media (max-width: 768px) {
      .discount-bubble {
        bottom: 85px; 
        left: 50%;
        transform: translateX(-50%);
        padding: 6px 14px 6px 6px;
        white-space: nowrap;
      }
      .discount-bubble:hover {
        transform: translateX(-50%) translateY(-5px) scale(1.03);
      }
    }"""
text = re.sub(css_pattern, new_css, text, flags=re.DOTALL)

# Replace HTML
html_pattern = r'<div class="discount-bubble reveal" onclick="openDirectModal\(\'Seaside Luxury Apartment\'\)">\s*<span style="font-size: 18px;">🎁</span> <span data-i18n="nav-discount">15% Off - Book Direct!</span>\s*</div>'
new_html = """<div class="discount-bubble reveal" onclick="openDirectModal('Seaside Luxury Apartment')">
    <div class="bubble-icon">
      <svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
        <path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"></path>
        <line x1="7" y1="7" x2="7.01" y2="7"></line>
      </svg>
    </div>
    <div class="bubble-content">
      <span class="bubble-offer">15% Off</span>
      <span class="bubble-action">Book Direct</span>
    </div>
  </div>"""
text = re.sub(html_pattern, new_html, text, flags=re.DOTALL)

with open('/Users/eliaskotsias/Desktop/Seaside Photos/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Bubble enhanced successfully!")
