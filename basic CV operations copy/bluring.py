import os
import cv2

img = cv2.imread(os.path.join('.','image_221.jpg'))


# it blur the how much near pixels
k_size = 7
img_blur = cv2.blur(img, (k_size, k_size))
gussian_blur = cv2.GaussianBlur(img,(k_size, k_size),3)
median_blur = cv2.medianBlur(img,k_size)

cv2.imshow('img', img)
cv2.imshow('img_blur', img_blur)
cv2.imshow('gussian_blur', gussian_blur)
cv2.imshow('median_blur', median_blur)
cv2.waitKey(0)




