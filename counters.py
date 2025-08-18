import os
import cv2

img = cv2.imread(os.path.join('.','birds.png'))
cv2.imshow('img',img)
cv2.waitKey(0)