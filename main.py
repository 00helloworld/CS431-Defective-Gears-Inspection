import cv2
import pylab as plt
import numpy as np
from PIL import Image

src_gear = "src_gear.png"
processed_images_path = "gears_transformations/"

def make_ring(n, thickness = 2):
    small_ring = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (n - thickness, n - thickness))
    big_ring = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (n, n))
    res = np.array(big_ring)
    step = int(thickness/2)
    for i in range(n-thickness):
        for j in range(n-thickness):
            res[i+step][j+step] = small_ring[i][j] ^ big_ring[i+step][j+step]
    return  res

def save_np_as_image(image, name):
    pilImage = Image.fromarray(image)
    pilImage.save(processed_images_path + name)

img = cv2.imread(src_gear)

# 1. erosion with hole ring
hole_size = 97
hole_ring = make_ring(hole_size, 2)
erosion = cv2.erode(img, hole_ring, iterations=1)
save_np_as_image(erosion, '001_holesize=95.jpg')

# 2. dilatation with hole mask
hole_mask = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (hole_size, hole_size))

dilation = cv2.dilate(erosion, hole_mask)
save_np_as_image(dilation, '002_holemask=ellipse.jpg')

# 3. original image OR dilation - no more holes in gears
image3 = cv2.bitwise_or(img, dilation)
save_np_as_image(image3, '003.jpg')

# 4. opening with gear_body
gear_size = 277
gear_body = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (gear_size, gear_size))
image4 = cv2.morphologyEx(image3, cv2.MORPH_OPEN, gear_body)
save_np_as_image(image4, '004_gear_size=277.jpg')


# все что выше - ок, нужно менять то, что ниже
# 5. dilate image4 with sampling_ring_spacer
ring_spacer_size = 13
sampling_ring_spacer = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (ring_spacer_size, ring_spacer_size))
image5 = cv2.dilate(image4, sampling_ring_spacer)
save_np_as_image(image5, '005_ring_spacer_size=13.jpg')

# 6.

ring_width_size = 21;
sampling_ring_width= cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (ring_width_size, ring_width_size))
image6 = cv2.dilate(image5, sampling_ring_width)
save_np_as_image(image6, '006_ring_spacer_width=21.jpg')

# 7.
image7 = cv2.bitwise_xor(image5, image6)
save_np_as_image(image7, '007.jpg')

# 8.
image8 = cv2.bitwise_and(img, image7)
save_np_as_image(image8, '008_original_XOR_007.jpg')





