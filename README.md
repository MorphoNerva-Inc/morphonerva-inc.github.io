# MorphoNerva, Inc. — Public Website (`morphonerva-inc.github.io`)

This repository powers the official public website of **MorphoNerva, Inc.**, served via GitHub Pages at:
👉 **[https://morphonerva-inc.github.io](https://morphonerva-inc.github.io)**

## Architecture & Design
- **Static, fast, zero runtime build dependencies:** Pure semantic HTML5, modern CSS3 with custom properties, and lightweight vanilla JavaScript.
- **Light & Dark Theme:** Automatic system preference detection (`prefers-color-scheme`) with manual toggle persisted across visits (`localStorage`).
- **Responsive:** Mobile-first layout, touch-friendly tap targets, and accessible navigation.
- **Verified Imagery:** Real, representative photographs from Wikimedia Commons and U.S. Government public domain (DARPA, NASA, DOE, NIST) with full attribution recorded in [`SOURCES.md`](SOURCES.md).
- **Public Disclosure Policy:** Strictly adheres to MorphoNerva's public disclosure guidelines — block-level architectures only, no trade secrets, no internal mechanisms, and no unmeasured performance claims.

## Structure
```
morphonerva-inc.github.io/
├── index.html                   # Homepage
├── technology/
│   └── index.html               # High-level architecture, event-driven theory, applications
├── research/
│   └── index.html               # Research questions, engineering standards, verification flow
├── roadmap/
│   └── index.html               # Milestone roadmap, Evidence Ladder policy
├── collaborate/
│   └── index.html               # Pilot partners, academic collaboration, engineering roles
├── contact/
│   └── index.html               # Public contact routes, corporate SAM.gov status
├── 404.html                     # Custom 404 page
├── assets/
│   ├── css/style.css            # Stylesheet (light/dark variables, responsive grid)
│   ├── js/main.js               # Theme switch, responsive nav toggle
│   └── images/                  # Real imagery and architectural vector diagrams
├── SOURCES.md                   # Complete image licensing and provenance register
├── CNAME.example                # Template for future custom domain configuration
└── README.md
```

## Custom Domain Preparation
When the custom domain is purchased by the founder, configure:
1. Rename or copy `CNAME.example` to `CNAME` with the apex domain (e.g., `morphonerva.com`).
2. Add DNS records (GitHub Pages A records for apex and CNAME for `www`).
3. Enable "Enforce HTTPS" in repository Settings &rarr; Pages.
