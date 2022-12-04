import cv2
import numpy as np
# reading an image
img = cv2.imread("image/flower.jpg")
# img = cv2.imread("image/image1.jpg")
# img = cv2.imread("image/image2.jpg")
# img = cv2.imread("image/image3.jpg")
# img = cv2.imread("image/image4.jpg")
# img = cv2.imread("image/image5.jpg")
# img = cv2.imread("image/image6.jpg")
# img = cv2.imread("image/image7.jpg")
# img = cv2.imread("image/image8.jpg")
# img = cv2.imread("image/image9.jpg")
print(type(img))
print(img.shape)
cv2.imshow("window",img)
cv2.waitKey(0)
