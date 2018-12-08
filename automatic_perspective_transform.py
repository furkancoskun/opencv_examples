import cv2
import numpy as np

image = cv2.imread('/home/frkn/Desktop/fotolar/solalt.png')
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

image_gray = np.float32(image_gray)
dst = cv2.cornerHarris(image_gray,2,3,0.04)

dst = cv2.dilate(dst,None)

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

pts1 = np.float32([[solust_x,solust_y],[sagust_x,sagust_y],[solalt_x,solalt_y],[sagalt_x,sagalt_y]])
pts2 = np.float32([[0,0],[1000,0],[0,1000],[1000,1000]])

M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(image,M,(1000,1000))

cv2.imwrite('/home/frkn/Desktop/fotolar/labirent_norm.png',dst)
