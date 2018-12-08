import cv2
import numpy as np

image = cv2.imread('/home/frkn/Desktop/fotolar/erosion.png',0)
img = cv2.bilateralFilter(image,8,70,70)
ret, threshold = cv2.threshold(img,75,255,cv2.THRESH_BINARY)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(threshold,kernel,iterations=1)
dilation = cv2.dilate(threshold,kernel,iterations=1)
cv2.imwrite('threshold_erosion.png',erosion)
while True :
    cv2.imshow('threshold',threshold)
    cv2.imshow('image',img)
    cv2.imshow('erosion',erosion)
    cv2.imshow('dilation',dilation)
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()

