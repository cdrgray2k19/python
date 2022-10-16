import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

import glob
import os

list_of_files = glob.glob('/Users/charliegray/Pictures/Photo Booth Library/Pictures/*') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)

img = cv.imread(latest_file)
#img = cv.imread('/Users/charliegray/Downloads/TEST2.jpg')
original = img

img = cv.bilateralFilter(img,30,75,75)

Z = img.reshape((-1,3))
# convert to np.float32
Z = np.float32(Z)
# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)

K = 4


''' elbow method to to get value of K for number of centres
compactness = []
for i in range(1,11):
    ret,label,center=cv.kmeans(Z,i,None,criteria,10,cv.KMEANS_PP_CENTERS)    
    compactness.append(ret)
print(compactness)'''


ret,label,center=cv.kmeans(Z,K,None,criteria,10,cv.KMEANS_PP_CENTERS)
# Now convert back into uint8, and make original image
center = np.uint8(center)

res = center[label.flatten()]
res2 = res.reshape((img.shape))

'''
for blurring out values that arent near to orange
for i in range(0,round(len(res2))):
    for j in range(0, round(len(res2[i]))):
        if res2[i][j][2] > 200  or res2[i][j][2] < 100:
            res2[i][j] = np.array([0,0,0])'''

gray = cv.cvtColor(res2, cv.COLOR_BGR2GRAY)

ret,thresh1 = cv.threshold(gray,100,255,cv.THRESH_BINARY)

contours, hierarchy = cv.findContours(thresh1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contours, -1, (0,255,0), 2)
maxArea = 0
maxIndex = 0
for i in range(0, len(contours)):
    area = cv.contourArea(contours[i])
    if area > maxArea:
        maxArea = area
        maxIndex = i

coneCnt = contours[maxIndex]

x,y,w,h = cv.boundingRect(coneCnt)
foreground = original[y:y+h, x:x+w]
cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),10)

cv.imshow('crop', foreground)

cv.imshow('original', original)
cv.imshow('image', img)
cv.imshow('res2',res2)

cv.imshow('thresh', thresh1)
#cv.imshow('edges', edges)
#cv.imshow('dilation', dilation)
cv.waitKey(0)
cv.destroyAllWindows()