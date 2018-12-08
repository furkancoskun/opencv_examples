import numpy as np
import imutils
import cv2
import time
import os
import serial

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
            
            #cv2.imwrite('/home/pi/opencv_examples/kayit/ucus/stitch_V4_{}.jpg'.format(j),result)
            #j = j+1
##########            for i in range(result.shape[0]):
##########                if (result[i,800,0] != 0) :
##########                    border=np.append(border,i)
##########            min_border = int(min(border))
##########            max_border = int(max(border))
##########            result = result[min_border:max_border,0:result.shape[1]]
####            
####            grayscale = cv2.cvtColor(result,cv2.COLOR_BGR2GRAY)
####            ret, threshold = cv2.threshold(grayscale,100,255,cv2.THRESH_BINARY)
##            image2, contours, hierarchy = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
##                    ##cnt = sorted(contours,key=cv2.contourArea,reverse=True)[:5]
##            contour_sizes=[(cv2.contourArea(contour),contour)for contour in contours]
##            biggest_contour = max(contour_sizes,key=lambda x: x[0])[1]
##            cv2.drawContours(result,biggest_contour,-1,(0,255,0),3)
##            x,y,w,h = cv2.boundingRect(biggest_contour)
##
##            result_2 = result[y:y+h,x:x+w]
            #cv2.imshow('threshold',threshold)
            cv2.imshow('result',result)
######            cv2.imshow('threshold',threshold)

            #cv2.imshow('result-2',result_2)
##    cv2.imshow('rpi',image2)
##    cv2.imshow('usb',image1)        

    cap.release()
    cap1.release()
    
    
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
    
cv2.destroyAllWindows()
