import os 
import cv2


img = cv2.imread(os.path.join('.','image_221.jpg'))
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('img',img)
cv2.imshow('img_rgb',img_rgb)
cv2.imshow('gray', gray)
cv2.imshow('hsv_img', hsv_img)

cv2.waitKey(0)

#we can perform many more conversions 