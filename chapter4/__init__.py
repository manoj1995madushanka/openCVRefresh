# draw shapes
import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
#color whole window
#img[:] = 255,0,0

print(img.shape[1])
# draw line
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 2) # resource, begin point, end point , colour, hardness
# draw rectangle
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)
# draw rectangle fill color
cv2.rectangle(img, (255, 130), (250, 350), (155, 0, 255), 2, cv2.FILLED)
# draw circle
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)
# draw circle fill color
cv2.circle(img, (20, 5), 30, (255, 5, 0), 5,cv2.FILLED)
#put text
cv2.putText(img,"Text",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,245,0),3)

cv2.imshow("shape", img)
cv2.waitKey(0)
