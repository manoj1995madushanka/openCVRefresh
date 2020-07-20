# basic functions
import cv2
import numpy as np
print("chapter 2 - image filters")

img = cv2.imread("./../Resources/test.jpg")
kernal = np.ones((5,5),np.uint8)

imgeGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img,(9,9),0)
imgCanny = cv2.Canny(img,150,200) #source black white
imgDialation = cv2.dilate(imgCanny,kernal,iterations=1)
imgEroded = cv2.erode(imgDialation,kernal,iterations=1)

cv2.imshow("Original",img)
cv2.imshow("Gray",imgeGray)
cv2.imshow("GausianBlur",imgBlur)
cv2.imshow("Canny",imgCanny)
cv2.imshow("Dilate",imgDialation)
cv2.imshow("Erode",imgEroded)
cv2.waitKey(0)