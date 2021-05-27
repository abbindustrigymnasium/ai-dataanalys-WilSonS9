import cv2 as cv
import numpy as np
import os

imgs = []
im1 = cv.imread('./rabbits/1.png')
# i = 0
# for f in os.listdir('./rabbits'):
#     imgs.append(cv.imread('./rabbits/' + f))
#     i += 1

cv.imshow('Complete', im1)

# j = 0
# for i in range(len(imgDict)-1):
#     try:
#         j += 1
#         img2 = imgDict[j]
#         print('Doing operation:', j)
#         imgr = cv.bitwise_and(img1, img2, mask = None)
#     except:
#         print('Done!')

cv.waitKey(10)
cv.destroyAllWindows()