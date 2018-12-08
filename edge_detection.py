import cv2
import numpy as np

image = cv2.imread('/home/frkn/Desktop/fotolar/maze.jpg')
img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(img,75,255,cv2.THRESH_BINARY)
kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(img,kernel,iterations=1)

edges = cv2.Canny(img,50,200,None, 3)
cv2.imshow('canny',edges)
lines = cv2.HoughLines(edges,1,np.pi/180,10,None,0,0)
for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imwrite('houghlines3.jpg',img)
cv2.waitKey(0)
