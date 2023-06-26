import cv2 as cv

## To read a Image 
img = cv.imread('lena.jpg') # 0 is for loading it in grayscale mode
print(img) # Printing Img means shows the matrix formed by pixels in the image imported
print(img.min())

## To display an Image 
cv.imshow('image', img)

cv.waitKey(0) # This adds a delay time for which the window is shown. If '0' as parameter the windows runs until closed with mouse
cv.destroyAllWindows() # This function destroys all the windows

## To Write an image 
cv.imwrite('lena_copy.png', img)
