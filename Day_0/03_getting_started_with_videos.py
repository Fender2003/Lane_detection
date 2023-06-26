from cv2 import cv2 as cv

# Turing on the webcam using Videocapture(0)
cap = cv.VideoCapture(0) # We can also write 'Video_name' in the parameter and it would open that video from the currrent folder

# Adding Fourcc code to a variable
fourcc = cv.VideoWriter_fourcc(*'XVID') # Giving XVID Codec to fourcc variable

# Calling the VideoWrite Class to write a video
out = cv.VideoWriter('Output.avi', fourcc, 20.0, (640, 480)) # Takes filename, fourcc code, fps and dimension as parameters

while (cap.isOpened()): # cap.isOpened() checks if the object is created succussfully or not

    # Reading video frame by frame
    isSuccess, frame = cap.read() # cap.read checks if the frame is read correctly and returns true and stores in isSuccess

    if isSuccess == True:
        # Printing the Height and Width of the Frame
        print(cap.get(cv.CAP_PROP_FRAME_WIDTH), end=" ")
        print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

        # Writing frame by frame to the out object
        out.write(frame) # Writes frame obtained to the out object

        # Converts frame into gray color
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        cv.imshow('Video', gray)

        if (cv.waitKey(1) & 0xFF) == ord('q'):
            break
        else:
            break

cap.release() # This command release the webcam and makes it free to use anywhere else
out.release() # Releasing VideoWriter Object

cv.destroyAllWindows()
