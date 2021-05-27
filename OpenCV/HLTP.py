import numpy as np
import cv2 as cv

img = cv.imread('./images/road.jfif')
img = cv.resize(img, (int(img.shape[1] * 0.25), int(img.shape[0] * 0.25)))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 50, 150, apertureSize=3)
cv.imshow('edges', edges)
cv.imshow('first', img)
lines = cv.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=5)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv.imshow('lines', img)

cv.waitKey(0)
cv.destroyAllWindows()