import numpy as np
import cv2 as cv

img = cv.imread('./images/shapes.jpg')
imgGrey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thresh = cv.threshold(imgGrey, 242, 255, cv.THRESH_BINARY)
contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, True), True)
    cv.drawContours(img, [approx], 0, (0, 0, 0), 2)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    if len(approx) == 3:
        cv.putText(img, 'Triangle', (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 4:
        cv.putText(img, 'Rectangle', (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 5:
        cv.putText(img, 'Pentagon', (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 10:
        cv.putText(img, 'Star', (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    else:
        cv.putText(img, 'Circle', (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

cv.imshow('shapes', img)
cv.waitKey(0)
cv.destroyAllWindows()