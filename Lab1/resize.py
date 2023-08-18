import cv2

sample_image = cv2.imread(r"C:\Users\OSLAB\Documents\210962021\Lab1\sampleimg.jpg")

resized_image = cv2.resize(sample_image,(1280, 720))

cv2.imshow('Original Image',sample_image)
cv2.waitKey(0)
cv2.imshow('Resized Image',resized_image)
cv2.waitKey(0)