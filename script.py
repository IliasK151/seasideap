import re

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Chat intro
text = text.replace('👋 <span data-i18n="chat-intro">', '<span data-i18n="chat-intro">')

# 2. SVGs
globe_svg = '<svg class="lang-icon" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:-2px; margin-right:4px;"><circle cx="12" cy="12" r="10"></circle><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path><path d="M2 12h20"></path></svg>'
text = text.replace("🇬🇧 EN", globe_svg + "EN")
text = text.replace("🇩🇪 DE", globe_svg + "DE")
text = text.replace("🇬🇷 EL", globe_svg + "EL")

x_svg = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="#ef4444" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>'
text = text.replace("❌", x_svg + " ")

check_svg = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="#22c55e" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>'
text = text.replace("✅", check_svg + " ")

sun_small = '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:-3px; margin-right:4px;"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>'
text = text.replace("☀️", sun_small)

map_pin_small = '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:-3px; margin-right:4px;"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>'
text = text.replace("📍 Nearby Vibes", map_pin_small + "Nearby Vibes")

coffee_svg = '<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="var(--gold)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8h1a4 4 0 0 1 0 8h-1"></path><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"></path><line x1="6" y1="1" x2="6" y2="4"></line><line x1="10" y1="1" x2="10" y2="4"></line><line x1="14" y1="1" x2="14" y2="4"></line></svg>'
text = text.replace('<div class="vibe-icon">☕</div>', '<div class="vibe-icon">' + coffee_svg + '</div>')

umbrella_svg = '<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="var(--gold)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12h20"></path><path d="M12 12V22"></path><path d="M12 12C12 6.477 16.477 2 22 2V12"></path><path d="M12 12C12 6.477 7.523 2 2 2V12"></path><path d="M12 22h-3"></path></svg>'
text = text.replace('<div class="vibe-icon">🏖️</div>', '<div class="vibe-icon">' + umbrella_svg + '</div>')

salad_svg = '<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="var(--gold)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 2v7c0 1.1.9 2 2 2h4a2 2 0 0 0 2-2V2"></path><path d="M7 2v20"></path><path d="M21 15V2v0a5 5 0 0 0-5 5v6c0 1.1.9 2 2 2h3Zm0 0v7"></path></svg>'
text = text.replace('<div class="vibe-icon">🥗</div>', '<div class="vibe-icon">' + salad_svg + '</div>')

sunset_svg = '<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="var(--gold)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v8"></path><path d="m4.93 10.93 1.41 1.41"></path><path d="M2 18h20"></path><path d="m19.07 10.93-1.41 1.41"></path><path d="M22 22H2"></path><path d="m8 6 4-4 4 4"></path><path d="M16 18a4 4 0 0 0-8 0"></path></svg>'
text = text.replace('<div class="vibe-icon">🌅</div>', '<div class="vibe-icon">' + sunset_svg + '</div>')

stars_svg = '<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="var(--gold)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"></path><path d="M5 3v4"></path><path d="M19 17v4"></path><path d="M3 5h4"></path><path d="M17 19h4"></path></svg>'
text = text.replace('<div class="vibe-icon">✨</div>', '<div class="vibe-icon">' + stars_svg + '</div>')

def loc_svg(path_str):
    return f'<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="var(--gold)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:-4px; margin-right:8px;">{path_str}</svg>'

plane = loc_svg('<path d="M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.2-1.1.7l1.3 5.3L3.2 14c-.3.3-.4.8-.2 1.2l3 3c.4.2.9.1 1.2-.2L9 16.2l5.3 1.3c.5-.2.8-.6.7-1.1z"></path>')
text = text.replace('✈️ ', plane)

umbrella_small = loc_svg('<path d="M2 12h20"></path><path d="M12 12V22"></path><path d="M12 12C12 6.477 16.477 2 22 2V12"></path><path d="M12 12C12 6.477 7.523 2 2 2V12"></path><path d="M12 22h-3"></path>')
text = text.replace('🏖️ ', umbrella_small)

landmark = loc_svg('<polygon points="12 2 2 7 22 7 12 2"></polygon><polyline points="2 17 2 22 22 22 22 17"></polyline><line x1="6" y1="7" x2="6" y2="17"></line><line x1="10" y1="7" x2="10" y2="17"></line><line x1="14" y1="7" x2="14" y2="17"></line><line x1="18" y1="7" x2="18" y2="17"></line>')
text = text.replace('🏛️ ', landmark)
text = text.replace('🛕 ', landmark)

utensils = loc_svg('<path d="M3 2v7c0 1.1.9 2 2 2h4a2 2 0 0 0 2-2V2"></path><path d="M7 2v20"></path><path d="M21 15V2v0a5 5 0 0 0-5 5v6c0 1.1.9 2 2 2h3Zm0 0v7"></path>')
text = text.replace('🍴 ', utensils)

cart = loc_svg('<circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path>')
text = text.replace('🛒 ', cart)

phone = loc_svg('<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>')
text = text.replace('📞 ', phone)

camera = loc_svg('<rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>')
text = text.replace('📷 ', camera)

# Address data-i18n replacements
text = text.replace('<p style="font-size:14px;color:var(--text-dark);font-weight:600" data-i18n="loc-addr">📍 Kremasti, Rhodes', 
              '<p style="font-size:14px;color:var(--text-dark);font-weight:600">' + map_pin_small + '<span data-i18n="loc-addr">Kremasti, Rhodes</span>')
text = text.replace('📍 Kremasti, Rhodes Island, Greece, 85101', 'Kremasti, Rhodes Island, Greece, 85101')
text = text.replace('📍 Kremasti, Insel Rhodos, Griechenland, 85101', 'Kremasti, Insel Rhodos, Griechenland, 85101')
text = text.replace('📍 Κρεμαστή, Ρόδος, Ελλάδα, 85101', 'Κρεμαστή, Ρόδος, Ελλάδα, 85101')

# Toast text block emojis
text = re.sub(r'"🇩🇪 ([^"]+)"', r'"\1"', text)
text = re.sub(r'"🇬🇧 ([^"]+)"', r'"\1"', text)
text = re.sub(r'"🔥 ([^"]+)"', r'"\1"', text)
text = re.sub(r'"✨ ([^"]+)"', r'"\1"', text)

# Add bell icon to toast markup
toast_old = '''<div id="social-proof-toast" class="social-proof-toast">
    <div class="sp-text" id="sp-text">Someone just booked for August!</div>
  </div>'''
bell_svg = '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="var(--gold)" stroke-width="2" style="margin-right:10px;"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg>'
toast_new = f'''<div id="social-proof-toast" class="social-proof-toast">
    {bell_svg}
    <div class="sp-text" id="sp-text">Someone just booked for August!</div>
  </div>'''
text = text.replace(toast_old, toast_new)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Emojis replaced in index.html")
