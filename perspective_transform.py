import cv2
import numpy as np

cıktıBoyut = 1050

img = cv2.imread('/home/frkn/Desktop/fotolar/maze_threshold1.jpg',0)

pts1 = np.float32([[950,161],[1810,226],[860,755],[2055,805]])
pts2 = np.float32([[0,0],[cıktıBoyut,0],[0,cıktıBoyut],[cıktıBoyut,cıktıBoyut]])

M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(cıktıBoyut,cıktıBoyut))
kernel = np.ones((70,70),np.uint8)
dilation = cv2.erode(dst,kernel,iterations=1)
dlted=dilation.copy()
np.asarray(dlted)

maze = np.divide(dilation.reshape(15,70,15,70).sum(axis=(1,3)),4900)

a = 100
maze[ maze <= a ] = 1
maze[ maze > a ] = 0

print(maze)
cv2.imwrite('0.jpg',dst)
cv2.imwrite('1.jpg',dilation)
while True:
    cv2.imshow('result',dst)
    cv2.imshow('original',img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
