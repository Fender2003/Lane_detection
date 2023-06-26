## Summing it all up

from cv2 import cv2 as c

# Reading an Image
img = c.imread('lena.jpg', 1)
print(img) 

## Displaying an Image 
c.imshow('image', img)
# waitkey() returns the unicode value of the key pressed on the keyboard 
key_pressed = c.waitKey(0) & 0xFF # We use 0xFF to binary and the last 8 bits of waitkey as it can return values upto 32bit

if key_pressed == '27': # 27 is the unicode for Escape Key
    c.destroyAllWindows() 
elif key_pressed == ord('s'): # ord() function returns the unicode of the string entered
    c.destroyAllWindows()
