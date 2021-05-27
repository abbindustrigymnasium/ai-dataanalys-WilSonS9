import numpy as np
import cv2 as cv
import matplotlib.pylab as plt

def RoI(imag, vertices):
    mask = np.zeros_like(imag)
    matchMaskColor = 255
    cv.fillPoly(mask, vertices, matchMaskColor)
    maskImag = cv.bitwise_and(imag, mask)
    return maskImag

cap = cv.VideoCapture('lanes.mp4')
while cap.isOpened():
    ret, img = cap.read()
    if ret == True:
        # img = cv.imread('./images/road.jfif')
        # img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        height = img.shape[0]
        width = img.shape[1]

        regionOfInterestVertices = [
            (0, height),
            (0, height - 10),
            (width/2, 2*height/3 + 15),
            (width, height)
        ]

        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        edges = cv.Canny(gray, 50, 200, L2gradient = True)

        newImg = RoI(edges, np.array([regionOfInterestVertices], np.int32))

        lines = cv.HoughLinesP(newImg, 1, np.pi / 180, 20, minLineLength=1, maxLineGap=35)

        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv.line(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
        cv.imshow('feed', img)
        if cv.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv.destroyAllWindows()