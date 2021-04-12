import numpy as np
import cv2

img = cv2.imread('images/rubberwhale1.png', -1)
img2 = cv2.imread('images/starry_star.png', -1)

print(img.shape)
print(img.size)
print(img.dtype)
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img, (512, 512))

img3 = cv2.addWeighted(img, .2, img2, .8, 1)

cv2.imshow('image', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()