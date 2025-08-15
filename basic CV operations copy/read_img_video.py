import cv2
import os 
# read image
img_path = os.path.join('.','image_221.jpg' )
img = cv2.imread(img_path)
print(type(img))
print(img.shape)


# write image
cv2.imwrite(os.path.join('.','image_out.jpg' ), img)


# visulize image
cv2.imshow("Frame",img)
cv2.waitKey(500)
cv2.destroyAllWindows()

# same process on video 
# read Video
video_path = os.path.join('.', 'demo.mp4')
video = cv2.VideoCapture(video_path)

# Visulize video 

# ret = True
# while ret:
#     ret , frame = video.read()

#     if ret:
#         # print("video is showing")
#         cv2.imshow('frame',frame)
#         cv2.waitKey(40)

# video.release
# cv2.destroyAllWindows()
# print("video is complete")


# video capture using webcame

webcame = cv2.VideoCapture(0)


# visulization webcame

while True:
    ret, frame = webcame.read()

    cv2.imshow("frame",frame)
    if cv2.waitKey(40) & 0xFF ==ord('q'):
        break


webcame.release()
cv2.destroyAllWindows()






