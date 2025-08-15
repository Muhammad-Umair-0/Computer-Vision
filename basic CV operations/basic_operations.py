import os 
import cv2
import matplotlib.pyplot as plt


img  = cv2.imread(os.path.join('.','image_out.jpg'))
resize_img  = cv2.resize(img,(700,600))


print(img.shape)
print(resize_img.shape)




cv2.imshow('image',img)
cv2.imshow("resized_img", resize_img)

plt.title("plt")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for correct display
plt.axis('off')  # Optional: Hide axis
plt.show()       # Show the image window

# image cropping
# img(y1:y2, x1:x2)
# y determines row y1 to y2
# x detemines columns x1-x2
cropped_img = img[180:307, 124:495]
cv2.imshow('cropped',cropped_img)
cv2.waitKey(0)
