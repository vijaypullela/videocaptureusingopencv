import cv2
video=cv2.VideoCapture(0)
while True:
    value,img=video.read()
    cv2.imshow("video stream",img)
    if cv2.waitKey(10)==ord('i'):
        break
video.release()
cv2.destroyAllWindows()
