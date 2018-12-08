import math
import cv2
import numpy as np

src = cv2.imread("/home/frkn/Desktop/1.jpg",0)

dst = cv2.Canny(src, 30, 180, None, 3)


cdst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)


lines = cv2.HoughLines(dst, 0.5, np.pi / 360, 150, None,0,0)

if lines is not None:
	for i in range (0, len(lines)):
	    rho = lines[i][0][0]
	    theta = lines[i][0][1]
	    a = math.cos(theta)
	    b = math.sin(theta)
	    x0 = a * rho
	    y0 = b * rho
	    pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
	    pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
	    cv2.line(cdst, pt1, pt2, (0,0,255), 3, cv2.LINE_AA)

while True:
	cv2.imshow('canny',dst)
	cv2.imshow("Source", src)
	cv2.imshow("Detected Lines (in red) - Standard Hough Line Transform", cdst)

	if cv2.waitKey(10) & 0xFF==ord('q'): 
		break
cv2.destroyAllWindows()

		

