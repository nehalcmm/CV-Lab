import cv2

sample_image = cv2.imread(r"C:\Users\OSLAB\Documents\210962021\Lab1\sampleimg.jpg",0)

cv2.imshow('Sample Image',sample_image)

cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.imwrite(r"C:\Users\OSLAB\Documents\210962021\Lab1\sampleimg1.jpg",sample_image)