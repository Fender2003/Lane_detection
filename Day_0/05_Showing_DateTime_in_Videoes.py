from cv2 import cv2 as cv
import datetime as dt 

cap = cv.VideoCapture(0)

# Getting Height and Width
print(cap.get(3)) # Width
print(cap.get(4)) # Height

while (cap.isOpened()):
    isSuccess, frame = cap.read()

    if isSuccess:

        # Adding Text to the frame
        font = cv.FONT_HERSHEY_SIMPLEX
        text = f"Width: {cap.get(3)} Height: {cap.get(4)}"
        datet = str(dt.datetime.now())
        cv.putText(frame, datet, (10, 50), font, 1, (0, 255, 255), 2, cv.LINE_AA)

        cv.imshow('Video', frame)

        if ((cv.waitKey(1) & 0xFF) == ord('q')):
            break

cap.release()
cv.destroyAllWindows()