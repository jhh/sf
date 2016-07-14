import cv2
import numpy as np
#Read Image
img = cv2.imread('python.jpg')
#Display Image
cv2.imshow('image',img)
cv2.waitKey(0)

#Applying Grayscale filter to image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('grayscale python',gray)
cv2.waitKey(0)

# close windows
cv2.destroyAllWindows()

#Saving filtered image to new file
cv2.imwrite('gray_python.jpg',gray)
