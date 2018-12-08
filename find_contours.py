import cv2
import numpy as np
import imutils

imag = cv2.imread('/home/frkn/Desktop/fotolar/solalt.png')
image = cv2.cvtColor(imag,cv2.COLOR_BGR2GRAY)
imag = imutils.resize(imag,width=750)
image = imutils.resize(image,width=750)
filtered_image= cv2.bilateralFilter(image,11,17,17)
canny = cv2.Canny(filtered_image,100,150)
drawing = np.zeros(imag.shape,np.uint8)
drawing_2 = np.zeros(imag.shape,np.uint8)
image2,contours,hierarchy = cv2.findContours(canny.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours :
	cv2.drawContours(drawing_2,[cnt],-1,(0,255,0),3)
	cv2.imshow('output_2',drawing_2)

for cnt in contours :
	hull = cv2.convexHull(cnt)
	cv2.drawContours(drawing,[cnt],-1,(0,255,0),3)
	cv2.drawContours(imag,[hull],-1,(0,255,0),3)	
	cv2.imshow('output',drawing)

print(len(contours))
print (contours)
#print(len(selected_contour))
cv2.imshow('original',imag)
cv2.imshow('filtered image',filtered_image)
cv2.imshow('canny',canny)
cv2.waitKey(0)
