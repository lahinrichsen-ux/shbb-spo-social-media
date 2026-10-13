"""SHBB-SPO Bildlook (Standard ab 13.10.2026): freundlicheres Licht, kräftigere Farben.
Aufruf: python bildlook.py eingabe.jpg ausgabe.jpg"""
import sys, numpy as np
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
im=ImageOps.exif_transpose(Image.open(sys.argv[1])).convert('RGB')
im=ImageOps.autocontrast(im,cutoff=0.5)
a=(np.asarray(im).astype(float)/255)**0.85
a[...,0]*=1.04; a[...,2]*=0.97
im=Image.fromarray((np.clip(a,0,1)*255).astype(np.uint8))
im=ImageEnhance.Color(im).enhance(1.35); im=ImageEnhance.Contrast(im).enhance(1.08)
im.filter(ImageFilter.UnsharpMask(radius=2,percent=60,threshold=3)).save(sys.argv[2],quality=92)
