import cv2

def get_hsv_range(color_name):
    """
    Returns lower and upper HSV limits for a given color name.
    Supported: 'red', 'green', 'blue', 'yellow'
    """
    color_ranges = {
        'red':    [(0, 100, 100), (10, 255, 255)],    # Lower red range
        'green':  [(40, 40, 40), (70, 255, 255)],
        'blue':   [(100, 150, 0), (140, 255, 255)],
        'yellow': [(20, 100, 100), (30, 255, 255)]
    }
    return color_ranges.get(color_name.lower())

color = 'red'  # Change to 'green', 'blue', or 'yellow' as needed
hsv_range = get_hsv_range(color)
if hsv_range:
    lower_limit, upper_limit = hsv_range
else:
    raise ValueError("Color not supported")

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsvImage, lower_limit, upper_limit)
    cv2.imshow("frame", mask)
    cv2.imshow("original", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break       

cap.release()
cv2.destroyAllWindows()