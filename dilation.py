import cv2
import numpy as np

img = cv2.imread('labirent_normalized.png')
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations=1)
dilation = cv2.dilate(img,kernel,iterations=1)
cv2.imwrite('erosion.png',erosion)
cv2.imwrite('dilation.png',dilation)
