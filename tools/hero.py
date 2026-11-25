"""MorphoNerva hero illustration: seeded synthetic spike raster (not measured data)."""
import random, math, sys
random.seed(55)
W,H=1920,760
rows=46; x0=560; x1=W-40; y0=70; y1=H-70
dy=(y1-y0)/(rows-1)
out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Illustration: sparse spiking activity that bursts only when an input event arrives (synthetic data)">',
'<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#070b18"/><stop offset="0.6" stop-color="#0e1a3a"/><stop offset="1" stop-color="#1a1440"/></linearGradient>',
'<radialGradient id="g1" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#4493f8" stop-opacity="0.35"/><stop offset="1" stop-color="#4493f8" stop-opacity="0"/></radialGradient>',
'<radialGradient id="g2" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#f778ba" stop-opacity="0.30"/><stop offset="1" stop-color="#f778ba" stop-opacity="0"/></radialGradient>',
'<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="2.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>',
f'<rect width="{W}" height="{H}" fill="url(#bg)"/>']
events=[(900,330,0.0),(1330,470,0.0),(1660,250,0.0)]
for ex,ey,_ in events:
    out.append(f'<ellipse cx="{ex}" cy="{ey}" rx="260" ry="240" fill="url(#g1)"/>')
out.append('<ellipse cx="1330" cy="470" rx="220" ry="200" fill="url(#g2)"/>')
# faint row guides
for r in range(rows):
    y=y0+r*dy
    out.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" stroke="#8aa4d6" stroke-opacity="0.06" stroke-width="1"/>')
ticks=[]
for r in range(rows):
    y=y0+r*dy
    x=x0
    while x<x1:
        # local rate: background ~sparse, bursts near events in (x,y)
        rate=0.0026
        for ex,ey,_ in events:
            d=math.hypot((x-ex)/90,(y-ey)/150)
            rate+=0.11*math.exp(-d*d)
        x+=random.expovariate(rate) if rate>0 else 999
        if x<x1:
            near=max(math.exp(-(((x-ex)/90)**2+((y-ey)/150)**2)) for ex,ey,_ in events)
            col='#f778ba' if near>0.5 and random.random()<0.35 else ('#7ab8ff' if near>0.2 else '#5b78b8')
            op=0.35+0.65*near
            ticks.append(f'<line x1="{x:.1f}" y1="{y-dy*0.36:.1f}" x2="{x:.1f}" y2="{y+dy*0.36:.1f}" stroke="{col}" stroke-opacity="{op:.2f}" stroke-width="2.8" stroke-linecap="round"/>')
out.append('<g filter="url(#glow)">'+''.join(ticks)+'</g>')
# input event markers along the bottom axis
for ex,ey,_ in events:
    out.append(f'<line x1="{ex}" y1="{y1+26}" x2="{ex}" y2="{y1+44}" stroke="#f778ba" stroke-width="3" stroke-linecap="round"/>')
out.append(f'<line x1="{x0}" y1="{y1+35}" x2="{x1}" y2="{y1+35}" stroke="#8aa4d6" stroke-opacity="0.25" stroke-width="1"/>')
out.append('</svg>')
open(sys.argv[1],'w',encoding='utf-8').write('\n'.join(out))
print(len(ticks),'spikes')
