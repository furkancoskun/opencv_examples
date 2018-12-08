import cv2
import numpy as np
import serial 
import imutils
import time
import os

if os.path.exists('/dev/video')==False:
    path = 'sudo modprobe bcm2835-v4l2'
    os.system (path)
    
j = 0

##
##ser = serial.Serial(
##	port='/dev/ttyS0',
##	baudrate=115200,
##	parity=serial.PARITY_ODD,
##	stopbits=serial.STOPBITS_TWO,
##	bytesize=serial.SEVENBITS
##)
##
##ser.open()

sift = cv2.xfeatures2d.SURF_create()

white_weaker = np.array([0,0,150])
white_stronger = np.array([180,90,255])
black_weaker = np.array([0,0,0])
black_stronger = np.array([180,255,60])
border = np.zeros(0)

i = 0
#img = cv2.imread('/home/frkn/Desktop/orta.jpg',0) 
j=1
threshold = 60
orta = [0,0]
ser = serial.Serial(
	port='/dev/ttyS0',
	baudrate=115200,
	parity=serial.PARITY_ODD,
	stopbits=serial.STOPBITS_TWO,
	bytesize=serial.SEVENBITS
)
KYatay = 1
KDikey = 1

while True:
    
	cap = cv2.VideoCapture(0) # cap USB kamera olmalı <<0 numara USB kamera>>
	cap1 = cv2.VideoCapture(1) # cap1 raspberry kamerası olmalı <<1 numara raspbery pi kamera>>
	    x_border = np.zeros(0)
	_,image1=cap.read()
	_,image2=cap1.read()

	image1 = imutils.resize(image1, width = 800)
	image2 = imutils.resize(image2, width = 800)

	(keypointsA, descriptorsA) = sift.detectAndCompute (image1,None)
	(keypointsB, descriptorsB) = sift.detectAndCompute (image2,None)

	matcher = cv2.DescriptorMatcher_create("BruteForce") #BruteForce, BruteForce-L1 , BruteForce-Hamming, BruteForce-Hamming(2), FlannBased
	rawMatches = matcher.knnMatch(descriptorsA, descriptorsB, 2) # k değeri farklı bir integer da olabilir

	kpsA = np.float32([kp.pt for kp in keypointsA])
	kpsB = np.float32([kp.pt for kp in keypointsB])

	matches = []
	ratio = 0.5
	reprojThresh =10

	for m in rawMatches:
		if len(m) == 2 and m[0].distance < m[1].distance * ratio:
		    matches.append((m[0].trainIdx, m[0].queryIdx))

	if len(matches) > 10:
		ptsA = np.float32([kpsA[i] for (_, i) in matches])
		ptsB = np.float32([kpsB[i] for (i, _) in matches])
		(H, status) = cv2.findHomography(ptsA, ptsB, cv2.LMEDS , reprojThresh)
		result = cv2.warpPerspective(image1, H,(image1.shape[1] + image2.shape[1], max( image1.shape[0], image2.shape[0])))
		result[result[:,:,:]==0]=255

		cv2.imshow('USB',result)

		USB_grayscale = cv2.cvtColor(result,cv2.COLOR_BGR2GRAY)
		ret, result = cv2.threshold(USB_grayscale,75,255,cv2.THRESH_BINARY)

		RPi_grayscale = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
		ret, image2 = cv2.threshold(RPi_grayscale,100,255,cv2.THRESH_BINARY)
			
		result[0:image2.shape[0], 0:image2.shape[1]] = image2

		cv2.imshow('result',result)
      

	cap.release()
	cap1.release()
    

	img = result.copy()



	x = 0
	y = 0
	totalMass = 1
	img1 = np.asarray(img, dtype = np.int32)


#	resmin orta noktasına referanslıyoruz drone'u
	orta[1]=int(len(img1)/2)
	orta[0]=int(len(img1[0])/2)


#	thresholddan küçük değerlere sahip pixellerin indisleri toplamı 
	x = np.sum(np.nonzero(img1<threshold)[1],None,"int64")
	y = np.sum(np.nonzero(img1<threshold)[0],None,"int64")


#	resmi thresholdlama
	img1[img1<threshold] = 1
	img1[img1>=threshold] = 0
	img[img>=threshold] = 255
	img[img<threshold] = 0

#	değeri 1 olan pixel sayısı
	totalMass = np.count_nonzero(img1)
	if(totalMass == 0):
		totalMass=1

#	ağırlık merkezi
	x = int(x / totalMass)
	y = int(y / totalMass)
	print("x:")
	print (x)
	print("y:")
	print(y)
	print("totalMass:")
	print(totalMass)

#	bulunan noktaları işaretleme
	cv2.circle(img, (x,y) ,5, (threshold,threshold,threshold),-1)
	cv2.circle(img, (orta[0],orta[1]) ,3, (0,0,0),-1)

#	ihaya komut gönderme
	fbYatay = int((x-orta[0]) * KYatay)
	fbDikey = int((y-orta[1]) * KDikey)
	print (fbYatay)
	print (fbDikey)
	if(fbDikey < 0 and fbYatay < 0):
		for i in range(-fbDikey):
#			serial.write("W")
			print("W")
		for i in range(-fbYatay):
#			serial.write("A")
			print("A")
	elif(fbDikey > 0 and fbYatay < 0):
		for i in range(fbDikey):
#			serial.write("S")
			print("S")
		for i in range(-fbYatay):
#			serial.write("A")
			print("A")
	elif(fbDikey < 0 and fbYatay > 0):
		for i in range(-fbDikey):
#			serial.write("W")
			print("W")
		for i in range(fbYatay):
#			serial.write("D")
			print("D")
	elif(fbDikey > 0 and fbYatay > 0):
		for i in range(fbDikey):
#			serial.write("S")
			print("S")
		for i in range(fbYatay):
#			serial.write("D")
			print("D")

	cv2.imshow('image',img)
##    if cv2.waitKey(1) & 0xFF == ord('a'):
##        cv2.imwrite('/home/pi/opencv_examples/maze_threshold{}.jpg'.format(j), img)
##        j = j+1
##        threshold = threshold + 5
##        time.sleep(0.5)
##    time.sleep(0.2)


