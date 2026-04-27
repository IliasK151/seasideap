# Love Stories – HTML/CSS/JS Version
### Luxury Wedding Planner · Rhodes, Greece

## How to Open

### Option A — Open directly in browser
Double-click `index.html` — works instantly, no setup needed.

### Option B — Local dev server (recommended)
```bash
# Python
python -m http.server 3000

# Node.js
npx serve .

# VS Code
Install "Live Server" extension → right-click index.html → Open with Live Server
```
Open `http://localhost:3000`

---

## File Structure

```
love-stories-html/
├── index.html          ← Main page (all sections)
├── css/
│   └── style.css       ← All styles, design tokens, responsive
├── js/
│   └── main.js         ← Cursor, scroll, animations, form, navbar
└── README.md
```

---

## Design Tokens (CSS Variables)

| Variable        | Value     | Usage           |
|-----------------|-----------|-----------------|
| `--cream`       | #F9F6F2   | Page background |
| `--white`       | #FFFFFF   | Section bg      |
| `--gold`        | #C6A96B   | Accent          |
| `--charcoal`    | #1A1A1A   | Text / dark bg  |
| `--muted`       | #8A8480   | Body text       |
| `--serif`       | Cormorant Garamond | Headings |
| `--sc`          | Cormorant SC | Labels / nav |
| `--sans`        | Jost      | Body copy       |

---

## Connecting the Contact Form

In `js/main.js`, find the `form.addEventListener('submit', ...)` block and replace the `console.log` with your preferred service:

### Option 1 – Formspree (free, no backend)
```html
<form id="contactForm" action="https://formspree.io/f/YOUR_ID" method="POST">
```

### Option 2 – EmailJS
```js
emailjs.send('SERVICE_ID', 'TEMPLATE_ID', data);
```

### Option 3 – Custom API
```js
const res = await fetch('/api/contact', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(data),
});
```

---

## Deploying

| Platform | Command |
|----------|---------|
| **Netlify** | Drag & drop the folder to netlify.com/drop |
| **Vercel** | `npx vercel` in the folder |
| **GitHub Pages** | Push to repo → Settings → Pages → root |
| **Any host** | Upload all files via FTP |

---

## Contact Details

- **Phone:** +30 693 290 8743  
- **Website:** lovestories.events  
- **Location:** Rhodes, Greece
