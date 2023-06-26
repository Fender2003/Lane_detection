import numpy as np
from cv2 import cv2 as cv

# Generating Image 1
img1 = np.zeros((250, 500, 3), np.uint8)
cv.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)

# Generating Image 2
img2 = np.full((250, 500, 3), 255, np.uint8)
cv.rectangle(img2, (0, 0), (250, 250), (0, 0, 0), -1)

# Performing Bitwise And Operation on both images
bitAnd = cv.bitwise_and(img2, img1) # Black acts as 0 and White acts as 1

# Performing Bitwise Or Operation on both images
bitOr = cv.bitwise_or(img2, img1) 

# Performing Bitwise Not Operation on both images
bitNot = cv.bitwise_not(img2)

# Performing Bitwise Xor Operation on both images
bitXor = cv.bitwise_xor(img2, img1) 

cv.imshow('image1', img1)
cv.imshow('image2', img2)
cv.imshow('bitAnd', bitAnd)
cv.imshow('bitOr', bitOr)
cv.imshow('bitNot', bitNot)
cv.imshow('bitXor', bitXor)

cv.waitKey(0)
cv.destroyAllWindows()