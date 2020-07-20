# resizing images
import cv2

img = cv2.imread("./../Resources/test.jpg")
print("original size : ",img.shape)
cv2.imshow("original",img)

imgResized = cv2.resize(img,(200,200))
print("rezised : ",imgResized.shape)
cv2.imshow("resized",imgResized)

imgCroped = img[0:200,200:400] #height wiidth
cv2.imshow("croped",imgCroped)
cv2.waitKey(0)
