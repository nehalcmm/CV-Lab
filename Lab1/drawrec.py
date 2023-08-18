import cv2

sample_image = cv2.imread(r"C:\Users\OSLAB\Documents\210962021\Lab1\sampleimg.jpg")

top_left = (100, 300)
bottom_right = (300, 200)
color = (0, 0, 0)
thickness = 2

cv2.rectangle(sample_image,top_left,bottom_right,color,thickness)

cv2.imshow('Rectangle Drawing',sample_image)
cv2.waitKey(0)
cv2.destroyAllWindows()