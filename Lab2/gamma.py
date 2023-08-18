import cv2
import numpy as np

image = cv2.imread(r"C:\Users\OSLAB\Documents\210962021\Lab2\rgbimage.jpg")

for gamma in [0.1,0.8,1.6,3.2]:
    gamma_corrected = np.array(255*(image/255) ** gamma,dtype = np.uint8)

    cv2.imshow("Gamma Corrected Image for value  "+str(gamma),gamma_corrected)
    cv2.waitKey(0)