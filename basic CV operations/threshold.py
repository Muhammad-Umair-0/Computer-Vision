import cv2
import os 


img = cv2.imread(os.path.join('.', 'panda.png'))
img = cv2.resize(img,(300,400))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img_gray,70,255, cv2.THRESH_BINARY)
# binary threshold 
thresh1 = cv2.blur(thresh,(10,10))
ret, thresh1 = cv2.threshold(thresh1,60,255, cv2.THRESH_BINARY)

#adaptive threshold
adaptive_thresh = cv2.adaptiveThreshold(
    img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30
)

cv2.imshow('img',img)
cv2.imshow('img_gray',img_gray)
cv2.imshow('thresh',thresh)
cv2.imshow('thresh1',thresh1)
cv2.imshow('adaptive_thresh',adaptive_thresh)
cv2.waitKey(0)