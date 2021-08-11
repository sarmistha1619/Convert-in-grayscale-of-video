import numpy as np
import cv2
capture = cv2.VideoCapture('VideoFromCamera.mp4')
def nothing(x):
    pass

cv2.namedWindow('sketch')
cv2.createTrackbar('a', 'sketch', 0, 10, nothing)
cv2.createTrackbar('b', 'sketch', 50, 100, nothing)
cv2.createTrackbar('c', 'sketch', 0, 300, nothing)
cv2.createTrackbar('d', 'sketch', 50, 150, nothing)
cv2.createTrackbar('e', 'sketch', 50, 150, nothing)


while(capture.isOpened()):
    ret, frame = capture.read()

    if ret== True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        a = cv2.getTrackbarPos('a', 'sketch')
        b = cv2.getTrackbarPos('b', 'sketch')
        c = cv2.getTrackbarPos('c', 'sketch')
        d = cv2.getTrackbarPos('d', 'sketch')
        e = cv2.getTrackbarPos('e', 'sketch')


        blur= cv2.GaussianBlur(gray, (5,5), a)

        canny =cv2.Canny(blur, b,c)
        ret, frame = cv2.threshold(canny, d, e, cv2.THRESH_BINARY_INV)
        cv2.imshow('sketch', canny)

        if cv2.waitKey(1000) & 0xFF==27:
            break
capture.release()
cv2.destroyAllWindows()