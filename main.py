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

# 1. errossion with hole ring
hole_size = 97
kernel = make_ring(hole_size, 4)
print("kernel:")
print(kernel)
print("==========================")
erosion = cv2.erode(img, kernel, iterations=1)
plt.imshow(erosion)
plt.show()
save_np_as_image(erosion, '001_holesize=97.jpg')
