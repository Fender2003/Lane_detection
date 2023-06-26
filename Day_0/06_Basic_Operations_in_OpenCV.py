import numpy as np
from cv2 import cv2 as cv

img = cv.imread('Data/messi5.jpg')
img2 = cv.imread('Data/opencv-logo.png')

print(img.shape) # returns a tuple of number of rows, columns, and channels
print(img.size) # returns the total number of pixels accessed
print(img.dtype) # returns the image data type is obtained

b, g, r = cv.split(img) # splits image into three channels and returns them
img = cv.merge((b, g, r)) # merges the three channels into onee image

# Copying the ball from one place to another
ball = img[280:340, 330:390] # here img[280:340, 330:390] represents a rectangle between x=(280,340) & y=(330,390)
img[273:333, 100:160] = ball # Copying the content of ball froom one place to another

# Adding two images **Note both the images must be of same sizes

#resizing images
img = cv.resize(img, (512,512))
img2 = cv.resize(img2, (512,512))

dst = cv.add(img, img2) # adds both the images
dst2 = cv.addWeighted(img, 1, img2, .5, 0) # adds img 100% and img2 50%

cv.imshow('Messi', dst2)
cv.waitKey(0)
cv.destroyAllWindows()

