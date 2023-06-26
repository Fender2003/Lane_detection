import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)


while True:
    isSuccess, frame = cap.read()
    frame = cv.resize(frame, (340, 240))
    
    if isSuccess:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        l_b = np.array([30, 20, 20])
        u_b = np.array([85, 255, 255])

        mask = cv.inRange(hsv, l_b, u_b)
        res = cv.bitwise_and(frame, frame, mask=mask)

        cv.imshow("Frame", frame)
        cv.imshow("Mask", mask)
        cv.imshow("HSV", hsv)
        cv.imshow("Res", res)

        key = cv.waitKey(1) & 0xFF

        if key == 27:
            break
    else:
        print("No Frames Read!")
        break

cap.release()
cv.destroyAllWindows()