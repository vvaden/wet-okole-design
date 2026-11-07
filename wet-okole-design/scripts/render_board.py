"""Portable, offline compositor. Source assets and current deliveries are immutable."""
from pathlib import Path
from PIL import Image, ImageFilter, ImageOps
import numpy as np
ROOT = Path(__file__).resolve().parents[1]

def render():
    # Use delivered layout to retain exact typography and captions.
    board = Image.open(ROOT/'current/latest-outer-circle-board.png').convert('RGB')
    blank = Image.open(ROOT/'assets/blank-charcoal-seats.png').convert('RGB')
    patch = Image.open(ROOT/'current/latest-outer-circle-emblem.png').convert('RGBA')
    hero = blank.resize((1696,1810), Image.Resampling.LANCZOS).convert('RGBA')
    for x,y,r,b in [(506,95,650,239),(194,164,254,246)]:
        p = patch.resize(((r-x)*2,(b-y)*2), Image.Resampling.LANCZOS)
        alpha = p.getchannel('A').filter(ImageFilter.GaussianBlur(1))
        shadow = Image.new('RGBA', p.size, (0,0,0,65))
        shadow.putalpha(alpha.point(lambda value:round(value*.22)))
        hero.alpha_composite(shadow,(x*2+1,y*2+2))
        hero.alpha_composite(p,(x*2,y*2))
    hero = hero.convert('RGB')
    assert np.array_equal(np.array(hero)[540:],np.array(blank.resize(hero.size,Image.Resampling.LANCZOS))[540:]), 'Seat panels changed'
    board.paste(hero,(0,0))
    detail = ImageOps.fit(hero.crop((860,0,1660,560)),(916,610),method=Image.Resampling.LANCZOS)
    board.paste(detail,(1708,0))
    out=ROOT/'rendered';out.mkdir(exist_ok=True)
    dest=out/'cloud-board-smoke-test.png';board.save(dest)
    print(f'Saved {dest.relative_to(ROOT)}; seat panels verified unchanged.')
    reference=Image.open(ROOT/'current/latest-outer-circle-board.png').convert('RGB')
    changed=int(np.any(np.array(board)!=np.array(reference),axis=2).sum())
    print(f'Pixels differing from delivered board: {changed} (library-version resampling can differ).')

if __name__ == '__main__': render()
