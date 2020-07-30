import os
from PIL import Image

def resize_image(img_dir, mwidth=500, mheight=300):
    image = Image.open(img_dir)
    w, h = image.size
    if w <= mwidth and h <= mheight:
        print(img_dir, 'is OK.')
        return
    if (1.0 * w / mwidth) > (1.0 * h / mheight):
        scale = 1.0 * w / mwidth
        new_im = image.resize((int(w / scale), int(h / scale)), Image.ANTIALIAS)

    else:
        scale = 1.0 * h / mheight
        new_im = image.resize((int(w / scale), int(h / scale)), Image.ANTIALIAS)
    new_im.save(img_dir)
    # new_im.close()
