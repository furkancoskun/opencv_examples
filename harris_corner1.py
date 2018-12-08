import cv2
import numpy as np

#np.set_printoptions(threshold=np.nan)
image = cv2.imread('/home/frkn/Desktop/fotolar/maze_threshold1.jpg')
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

image_gray = np.float32(image_gray)
dst = cv2.cornerHarris(image_gray,2,29,0.04)

dst = cv2.dilate(dst,None)
#coordinates = np.zeros(dst.shape)
		
image[dst>0.01*dst.max()] = [0,0,255]

coord = np.where(np.all(image == (0, 0, 255), axis=-1))
coord_sum = np.zeros(len(coord[0]))
coord_dif = np.zeros(len(coord[0]))
for i in range(len(coord[0])):
	coord_sum [i] = coord[0][i]+coord[1][i]
	coord_dif [i] = coord[0][i]-coord[1][i]

sagalt_y = coord[0][coord_sum.tolist().index(max(coord_sum))]
sagalt_x = coord[1][coord_sum.tolist().index(max(coord_sum))]
solust_y = coord[0][coord_sum.tolist().index(min(coord_sum))]
solust_x = coord[1][coord_sum.tolist().index(min(coord_sum))]
solalt_y = coord[0][coord_dif.tolist().index(max(coord_dif))]
solalt_x = coord[1][coord_dif.tolist().index(max(coord_dif))]
sagust_y = coord[0][coord_dif.tolist().index(min(coord_dif))]
sagust_x = coord[1][coord_dif.tolist().index(min(coord_dif))]

print("sagalt_y: {}" .format(sagalt_y))
print("sagalt_x: {}" .format(sagalt_x))
print("solust_y: {}" .format(solust_y))
print("solust_x: {}" .format(solust_x))
print("solalt_y: {}" .format(solalt_y))
print("solalt_x: {}" .format(solalt_x))
print("sagust_y: {}" .format(sagust_y))
print("sagust_x: {}" .format(sagust_x))
cv2.imshow('dst',image) 
cv2.waitKey(0)
#print(dst)
