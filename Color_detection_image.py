import cv2 as cv
import numpy as np

img = cv.imread('C:/Projekty/Color_Detection/data/zachod.jpg')
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

lower_range = (0, 50, 50) # lower range of red color in HSV
upper_range = (10, 255, 255) # upper range of red color in HSV

mask = cv.inRange(hsv_img, lower_range, upper_range)
color_image = cv.bitwise_and(img, img, mask=mask)

cv.imshow('Color image', color_image)
cv.waitKey(0)
cv.destroyAllWindows()