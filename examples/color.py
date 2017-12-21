import numpy as np
import cv2
from imageUtils import ColorUtils
import os

# load and show the image normally
image_folder = (os.path.join(os.getcwd(), "samples"))
m1 = cv2.imread(os.path.join(image_folder, "bb.jpeg"), 1)  # 1 = load color
m1BW = cv2.imread(os.path.join(image_folder, "bb.jpeg"), 0)  # 0= load b/w
cv2.imshow("m1", m1)
cv2.moveWindow('m1', 10, 10)

height, width, channels = m1.shape

cv2.imshow('grayscale', ColorUtils.convert_rbg_to_grayscale(m1))
cv2.moveWindow('grayscale', 10+width, 10)

cv2.imshow('recolored r g b', ColorUtils.color_sep_image(m1, 'rgb'))
cv2.moveWindow('recolored r g b', 10, 45+height)

cv2.imshow('recolored h s v', ColorUtils.color_sep_image(m1, 'hsv'))
cv2.moveWindow('recolored h s v', 10, 70+(2*height))

cv2.imshow('basic thresh', ColorUtils.basic_threshold(m1BW, 70))
cv2.moveWindow('basic thresh', 10+2*width, 10)

cv2.imshow('adaptive thresh', ColorUtils.adaptive_threshold(m1BW, 21))
cv2.moveWindow('adaptive thresh', 10+3*width, 10)

print("size: {}x{} channels: {}".format(width, height, channels))

cv2.waitKey(0)
cv2.destroyAllWindows()

rgba_image = ColorUtils.convert_rgb_to_rgba(m1)
cv2.imwrite("test.png", rgba_image)
