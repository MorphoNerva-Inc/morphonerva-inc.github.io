import sys, asyncio
from playwright.sync_api import sync_playwright
base, out = sys.argv[1], sys.argv[2]
pages = ["", "technology/", "research/", "roadmap/", "collaborate/", "contact/"]
with sync_playwright() as p:
    b = p.chromium.launch()
    for name, vp, mobile in [("desktop", {"width":1440,"height":900}, False), ("phone", {"width":390,"height":844}, True)]:
        ctx = b.new_context(viewport=vp, device_scale_factor=2 if mobile else 1, is_mobile=mobile, has_touch=mobile)
        pg = ctx.new_page()
        for path in pages:
            pg.goto(base + path, wait_until="networkidle")
            pg.wait_for_timeout(400)
            slug = path.strip("/") or "home"
            pg.screenshot(path=f"{out}/{slug}-{name}.png", full_page=True)
            # report image fit
            info = pg.evaluate("""() => [...document.images].map(i=>({src:i.currentSrc.split('/').pop(), nw:i.naturalWidth, nh:i.naturalHeight, w:Math.round(i.getBoundingClientRect().width), h:Math.round(i.getBoundingClientRect().height), fit:getComputedStyle(i).objectFit}))""")
            for i in info:
                if i['w']>60: print(name, slug, i)
        ctx.close()
    b.close()
