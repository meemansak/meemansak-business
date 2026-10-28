# Meemansak Bharti — Digital business card

Live website: https://meemansak.github.io/business-card/
Repository: https://github.com/meemansak/business-card

Independent static website. No build step or API keys required. Edit the website in `dist/`; pushing `main` to the `github` remote automatically deploys it through `.github/workflows/pages.yml`.

- `dist/index.html`: contact page
- `dist/style.css`: responsive visual design
- `dist/card.html`: business card source, 1200 × 700
- `dist/assets/business-card.png`: downloadable card, 2400 × 1400
- `dist/meemansak-bharti.vcf`: downloadable contact
- `dist/assets/connect-qr.png`: QR opening the GitHub Pages website

Local project folder: D:\Business card Website

To change the website address later, update `dist/app.js`, `dist/index.html`, `dist/card.html` and `make-qr.py`. Regenerate the QR and re-export the card. Already shared card images retain their original QR destination.

`make-qr.py` uses ReportLab and Pillow. `verify.cjs` uses this computer's Playwright and Chrome installation to export the card and check the layout. These are optional authoring tools; deployed pages have no runtime dependencies. Fonts and licenses are included in `dist/assets/`.
