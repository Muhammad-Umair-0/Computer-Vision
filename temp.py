import os
import cv2

img = cv2.imread(os.path.join('.', 'birds.png'))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# Use thresholded image for contour detection
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Remove unused sum calculation
box_count = 0
for con in contours:
    area = cv2.contourArea(con)
    print(area)
    if area > 200:  s
        x1, y1, w, h = cv2.boundingRect(con)
        cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)  # Green color
        box_count += 1

print("The total birds are", box_count)

cv2.imshow('img', img)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()