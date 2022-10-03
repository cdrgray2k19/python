import cv2 as cv
from cv2 import cvtColor
from cv2 import norm
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("/Users/charliegray/Downloads/TEST2.jpg", 0)


noiseRed = cv.fastNlMeansDenoising(img, None, 50, 7, 21)
#gray = cv.cvtColor(noiseRed, cv.COLOR_BGR2GRAY)


hist = cv.equalizeHist(noiseRed)

normalised = (hist - np.min(hist)) / (np.max(hist) - np.min(hist))

kernel = np.ones((5,5),np.uint8)
opening = cv.morphologyEx(normalised, cv.MORPH_OPEN, kernel)

resized = cv.resize(opening, (256, 256))

cv.imshow('img',img)
cv.imshow('norm',opening)
cv.imshow('resize',resized)
cv.waitKey(0)
cv.destroyAllWindows()