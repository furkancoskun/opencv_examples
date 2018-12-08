import cv2
import numpy as np
from scipy.signal import argrelextrema
from scipy.signal import find_peaks, peak_prominences
import time
image = cv2.imread('/home/frkn/Desktop/fotolar/dilation.png',0)
np.set_printoptions(threshold=np.nan)
print(image.shape)
horizontal_weight = np.zeros(image.shape[0])
vertical_weight = np.zeros(image.shape[1])
for i in range (0,image.shape[0]):
	for j in range (0,image.shape[1]):
		horizontal_weight[i] = horizontal_weight[i] + image[i][j] 
for j in range (0,image.shape[1]):
        for i in range (0,image.shape[0]): 
                vertical_weight[j] = vertical_weight[j] + image[i][j] 
horizontal_maxima_indexes = argrelextrema(horizontal_weight,np.greater)
horizontal_minima_indexes = argrelextrema(horizontal_weight,np.less)
vertical_maxima_indexes = argrelextrema(vertical_weight,np.greater)
vertical_minima_indexes = argrelextrema(vertical_weight,np.less)
peaks,_ = find_peaks(horizontal_weight)
prominences=peak_prominences(horizontal_weight,peaks)[0]
print("horizontal_maxima_indexes : {}".format(horizontal_maxima_indexes))
print("horizontal_minima_indexes: {}".format(horizontal_minima_indexes))
print("vertical_maxima_indexes : {}".format(vertical_maxima_indexes))
print("vertical_minima_indexes: {}".format(vertical_minima_indexes))
print("peak : {}".format(peaks))
print("prominence : {}".format(prominences))
#print(horizontal_weight)
#print(vertical_weight)

