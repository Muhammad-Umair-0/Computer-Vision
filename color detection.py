import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Typical HSV range for yellow
    lower_limit = (20, 100, 100)
    upper_limit = (30, 255, 255)

    mask = cv2.inRange(hsvImage, lower_limit, upper_limit)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:  # Filter small areas
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)  # Yellow box

    cv2.imshow("mask", mask)
    cv2.imshow("frame with bounding box", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break       

cap.release()
cv2.destroyAllWindows()