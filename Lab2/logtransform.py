import cv2
import numpy as np

image2 = cv2.imread(r"C:\Users\OSLAB\Documents\210962021\Lab2\log.jpg")

image = cv2.resize(image2,(640,480))
image1 = cv2.resize(image2,(640,480))

c = 255/(np.log(1+np.max(image)))
log_transformed = c * np.log(1 + image)

log_transformed = np.array(log_transformed,dtype = np.uint8)

cv2.imshow("Original Image",image1)
cv2.imshow("Log Transformed Image",log_transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()