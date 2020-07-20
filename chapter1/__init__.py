import cv2

print("chapter 1")


# read images
def imgRead():
    img = cv2.imread("./../Resources/test.jpg")
    cv2.imshow("Output", img)
    cv2.waitKey(0)


# read videos
def videoRead():
    vid = cv2.VideoCapture("./../Resources/video.webm")
    while True:
        success, img = vid.read()
        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


# record video from webcam
def webCamReacord():
    vidcam = cv2.VideoCapture(0)  # set id 0 for webcam
    vidcam.set(3, 640)  # height
    vidcam.set(4, 480)  # width
    vidcam.set(10, 100)  # brightness

    while True:
        success, img = vidcam.read()
        cv2.imshow("video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


#webCamReacord()
#videoRead()
imgRead()