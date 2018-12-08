import cv2
import numpy as np

#np.set_printoptions(threshold=np.nan)
image = cv2.imread('/home/frkn/Desktop/fotolar/labirent.png')
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

image_gray = np.float32(image_gray)
dst = cv2.cornerHarris(image_gray,2,3,0.04)

dst = cv2.dilate(dst,None)
#coordinates = np.zeros(dst.shape)
		
image[dst>0.01*dst.max()] = [0,0,255]

coord = np.where(np.all(image == (0, 0, 255), axis=-1))
coord_sum = np.zeros(len(coord[0]))
for i in range(len(coord[0])):
	coord_sum [i] = coord[0][i]+coord[1][i]

print("min_coord_sum: {}" .format(min(coord_sum)))
print("max_coord_sum: {}" .format(max(coord_sum)))

cv2.imshow('dst',image) 
cv2.waitKey(0)
#print(dst)
