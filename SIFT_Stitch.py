import numpy as np
import imutils
import cv2
import time

sift = cv2.xfeatures2d.SURF_create()
i = 0
#time.sleep
while True:
    cap = cv2.VideoCapture(0)
    cap1 = cv2.VideoCapture(1)
    _,image1=cap.read()
    _,image2=cap1.read()
    #image1 = imutils.resize(image1, width = 500)
    #image2 = imutils.resize(image2, width = 500)
    (keypointsA, descriptorsA) = sift.detectAndCompute (image1,None)
    (keypointsB, descriptorsB) = sift.detectAndCompute (image2,None)

    matcher = cv2.DescriptorMatcher_create("BruteForce") #flannbased bruteforce_l1 bruteforce_hamming bruteforce_hamminglut brutforce_sl2
    rawMatches = matcher.knnMatch(descriptorsA, descriptorsB, 2) # k değeri farklı bir integer da olabilir

    kpsA = np.float32([kp.pt for kp in keypointsA])
    kpsB = np.float32([kp.pt for kp in keypointsB])

    matches = []
    ratio = 0.5
    reprojThresh = 4

    for m in rawMatches:
            if len(m) == 2 and m[0].distance < m[1].distance * ratio:
                    matches.append((m[0].trainIdx, m[0].queryIdx))

    if len(matches) > 10:
            ptsA = np.float32([kpsA[i] for (_, i) in matches])
            ptsB = np.float32([kpsB[i] for (i, _) in matches])
            (H, status) = cv2.findHomography(ptsA, ptsB, cv2.LMEDS , reprojThresh)
            result = cv2.warpPerspective(image1, H,(image1.shape[1] + image2.shape[1], max( image1.shape[0], image2.shape[0])))
            result[0:image2.shape[0], 0:image2.shape[1]] = image2
            #print(H)
            cv2.imshow('result',result)
            #cv2.imwrite('/home/pi/opencv_examples/kayit/ucus/stitch_V2_{}.jpg'.format(i),result)
            i = i+1

    cv2.imshow('USB',image1)
    cv2.imshow('rpi',image2)
    #cv2.imwrite('/home/pi/opencv_examples/kayit/ucus/stitch_{}.jpg'.format(i),result)
    cap.release()
    cap1.release()
    
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
    
cv2.destroyAllWindows()


