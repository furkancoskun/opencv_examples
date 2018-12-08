import cv2
import numpy as np
import imutils

imag = cv2.imread('/home/frkn/Desktop/fotolar/eyup.jpg')
image = cv2.cvtColor(imag,cv2.COLOR_BGR2GRAY)
imag = imutils.resize(imag,width=750)
image = imutils.resize(image,width=750)
filtered_image= cv2.bilateralFilter(image,11,17,17)
canny = cv2.Canny(filtered_image,100,150)
drawing = np.zeros(imag.shape,np.uint8)
drawing_2 = np.zeros(imag.shape,np.uint8)
image2,contours,hierarchy = cv2.findContours(canny.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))

for cnt in contours :
	print(cv2.moments(cnt))

#print (contours)

#print(hierarchy)
#print(len(selected_contour))
