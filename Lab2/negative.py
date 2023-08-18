import cv2
import numpy as np

image = cv2.imread(r"C:\Users\OSLAB\Documents\210962021\Lab2\sampleimg.jpg")

negative_image = 255 - image

cv2.imshow("Negative Image",negative_image)
cv2.waitKey(0)


resized_image = cv2.resize(image,(1920, 1080))
cv2.imshow("Resized Image",resized_image)
cv2.waitKey(0)

rotated_image = cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Rotated Image",rotated_image)
cv2.waitKey(0)

cv2.ROTATE