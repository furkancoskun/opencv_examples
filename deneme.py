import cv2
import numpy as np

test = cv2.imread('/home/frkn/Desktop/fotolar/contour6.jpg')
while True :
    cv2.imshow('test',test)
    if cv2.waitKey(10) & 0xFF == ord('q'):
    	break
cv2.destroyAllWindows()
