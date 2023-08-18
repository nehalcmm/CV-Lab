import cv2

sample_image = cv2.imread(r"C:\Users\OSLAB\Documents\210962021\Lab1\sampleimg.jpg")

angle = 45

height ,width = 640,480

rotationmatrix = cv2.getRotationMatrix2D((width/2,height/2),angle,1)

rotatedimage = cv2.warpAffine(sample_image,rotationmatrix,(width,height))

cv2.imshow('Original Image',sample_image)
cv2.waitKey(0)

cv2.imshow('Rotated Image',rotatedimage)
cv2.waitKey(0)