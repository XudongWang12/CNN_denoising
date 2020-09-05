import cv2
from PIL import Image

for threshold in range(100, 240, 20):
    img = Image.open('G:\\gauss.png')
    img = img.convert("L")
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    img.save(str(threshold)+'.png')
