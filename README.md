# MorphoNerva, Inc. — Public Website (`morphonerva-inc.github.io`)

This repository powers the official public website of **MorphoNerva, Inc.**, served via GitHub Pages at:
👉 **[https://morphonerva-inc.github.io](https://morphonerva-inc.github.io)**

## Architecture & Standards
- **Static, fast, zero runtime build dependencies:** Pure semantic HTML5, modern CSS3 with custom properties, and lightweight vanilla JavaScript.
- **Light & Dark Themes:** Automatic system preference detection (`prefers-color-scheme`) with manual toggle persisted across visits (`localStorage`).
- **Responsive:** Mobile-first layout, touch-friendly tap targets, and accessible navigation.
- **Verified Imagery:** Real, representative photographs from Wikimedia Commons and U.S. Government public domain (DARPA, Cajal, NASA, U.S. Coast Guard, DOE) with full attribution recorded in [`SOURCES.md`](SOURCES.md).
- **Public Disclosure Policy:** Strictly adheres to MorphoNerva's public disclosure guidelines (`PUBLIC_DISCLOSURE_GUIDELINE.md`) — block-level architectures only, no trade secrets, no internal mechanisms, and no unmeasured performance claims.

## Structure
```
morphonerva-inc.github.io/
├── index.html                   # Home
├── technology/
│   └── index.html               # Technology (why event-driven, activity scaling, SNNs, platform, verification)
├── research/
│   └── index.html               # Research (open questions, engineering standards, reading list)
├── roadmap/
│   └── index.html               # Roadmap (stage-level milestones, Evidence Ladder policy)
├── collaborate/
│   └── index.html               # Collaborate (pilot partners, research, engineering roles, contribution rules)
├── contact/
│   └── index.html               # Contact (public collaboration form, SAM.gov status, security reporting)
├── 404.html                     # Custom 404 error page
├── assets/
│   ├── css/style.css            # Stylesheet (light/dark variables, responsive layout)
│   ├── js/main.js               # Theme switch, responsive nav toggle
│   ├── hero.jpg                 # Hero banner photo collage
│   ├── photos/                  # Real photos (DARPA board, Cajal, neuron, event camera, wind farm, buoy, spectrograph)
│   ├── *.svg                    # Architectural vector diagrams (*-light.svg / *-dark.svg pairs)
│   └── SOURCES.md               # Image licensing and provenance register
├── SOURCES.md                   # Root copy of image licensing register
├── robots.txt                   # Search crawler directives
└── README.md
```
