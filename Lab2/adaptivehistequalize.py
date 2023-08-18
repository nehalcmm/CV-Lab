import cv2
import numpy as np
import matplotlib as plt

image = cv2.imread(r"C:\Users\OSLAB\Documents\210962021\Lab2\grayscale.jpg")

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
clahe = cv2.createCLAHE(clipLimit = 5)
finalimg = clahe.apply(gray)

cv2.imshow("Original Image",image)
cv2.imshow("CLAHE Image",finalimg)
cv2.waitKey(0)
cv2.destroyAllWindows()