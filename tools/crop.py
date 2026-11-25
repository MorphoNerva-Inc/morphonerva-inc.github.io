import sys
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
raw, out = sys.argv[1], sys.argv[2]
# name, src, aspect (w,h), out width, focus x, focus y
jobs = [
 ("neuron-network-gfp.jpg","gfp",(21,9),2400,0.5,0.45),
 ("cerebellum-silver-stain.jpg","cereb",(4,3),1600,0.5,0.3),
 ("spinnaker-machine.jpg","spinn",(21,9),2400,0.5,0.5),
 ("silicon-wafer-12in.jpg","wafer",(21,9),2400,0.5,0.5),
 ("nasa-engineers-lab.jpg","lisa",(21,9),2400,0.5,0.5),
 ("mars-curiosity-remote-sensing.jpg","curio",(21,9),2400,0.5,0.35),
 ("neuromorphic-nanowire-network.jpg","nanowire",(4,3),1600,0.5,0.5),
]
for name,src,(aw,ah),ow,fx,fy in jobs:
    im = Image.open(f"{raw}/{src}.src").convert("RGB")
    if src=="nanowire":
        w0,h0=im.size; im=im.crop((int(w0*.04),int(h0*.06),int(w0*.96),int(h0*.80)))
    W,H = im.size; ar = aw/ah
    if W/H > ar: cw,ch = int(H*ar),H
    else: cw,ch = W,int(W/ar)
    x = min(max(int(fx*W-cw/2),0),W-cw); y = min(max(int(fy*H-ch/2),0),H-ch)
    c = im.crop((x,y,x+cw,y+ch))
    ow = min(ow,cw); c = c.resize((ow,round(ow/ar)),Image.LANCZOS)
    c.save(f"{out}/{name}",quality=84,optimize=True,progressive=True); print(name,c.size,cw,ch)
# prophesee: product shot on white -> 21:9 white canvas, camera centred (seamless background)
im = Image.open(f"{raw}/prophesee.src").convert("RGB")
canvas = Image.new("RGB",(2400,1029),(255,255,255))
h = 980; w = round(im.width*h/im.height); im = im.resize((w,h),Image.LANCZOS)
canvas.paste(im,((2400-w)//2,(1029-h)//2)); canvas.save(f"{out}/event-camera-kit.jpg",quality=84,optimize=True,progressive=True); print("event-camera-kit.jpg",canvas.size)
