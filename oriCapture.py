# A simple dynamic programming solution for finding the orientation 
# of a syringe from a bounding box.

import cv2
import numpy
from matplotlib import pyplot
    #           Q1 Q2 Q3
    #           Q4 Q5 Q6
    #           Q7 Q8 Q9

    # Essentially if the sum of Q1 and Q9 is 
    # greater than the sum of Q2 and Q8 and greater than the sum of Q3 and Q7 
    # and greater than the sum of Q4 and Q6 we know the syringe mus be oriented at a 135 
    # degree angle where zero is the syringe facing upward
def oriCapture(x,y,w,h,img):
    
    color_0 = cv2.imread(img,0)
    crop_color_0 = color_0[y:y+h, x:x+w]

    cv2.threshold(crop_color_0,x,y,cv2.THRESH_BINARY)
    crop_color_0[crop_color_0 < 144] = 0
    
    Q1 = 0
    Q2 = 0
    Q3 = 0
    Q4 = 0
    Q6 = 0
    Q7 = 0
    Q8 = 0
    Q9 = 0

    for i in range(0,int(numpy.rint(len(crop_color_0)/3))):
        for j in range(0,int(numpy.rint(len(crop_color_0[i])/3))):
            Q1 += crop_color_0[i][j]
    for i in range(int(numpy.rint(len(crop_color_0)/3) + 1), (int(2*numpy.rint(len(crop_color_0)/3)))):
        for j in range(0,int(numpy.rint(len(crop_color_0[i])/3))):
            Q2 += crop_color_0[i][j]
    for i in range((int(2*numpy.rint(len(crop_color_0))/3) + 1), int(numpy.rint(len(crop_color_0)))):
        for j in range(0,int(numpy.rint(len(crop_color_0[i])/3))):
            Q3 += crop_color_0[i][j]
    for i in range(0,int(numpy.rint(len(crop_color_0)/3))):
        for j in range(int(numpy.rint(len(crop_color_0[i])/3) + 1),(int(2*numpy.rint(len(crop_color_0[i]))/3))):
            Q4 += crop_color_0[i][j]
    for i in range((int(2*numpy.rint(len(crop_color_0))/3) + 1), int(numpy.rint(len(crop_color_0)))):
        for j in range(int(numpy.rint(len(crop_color_0[i])/3) + 1),(int(2*numpy.rint(len(crop_color_0[i]))/3))):
            Q6 += crop_color_0[i][j]
    for i in range(0,int(numpy.rint(len(crop_color_0)/3))):
        for j in range((2*int(numpy.rint(len(crop_color_0[i]))/3) + 1),int(numpy.rint(len(crop_color_0[i])))):
            Q7 += crop_color_0[i][j]
    for i in range(int(numpy.rint(len(crop_color_0)/3) + 1), (int(2*numpy.rint(len(crop_color_0))/3))):
        for j in range((int(2*numpy.rint(len(crop_color_0[i]))/3) + 1),int(numpy.rint(len(crop_color_0[i])))):
            Q8 += crop_color_0[i][j]
    for i in range((int(2*numpy.rint(len(crop_color_0))/3) + 1), int(numpy.rint(len(crop_color_0)))):
        for j in range((int(2*numpy.rint(len(crop_color_0[i]))/3) + 1),int(numpy.rint(len(crop_color_0[i])))):
            Q9 += crop_color_0[i][j]

    degrees_0 = Q2 + Q8
    degrees_45 = Q3 + Q7
    degrees_90 = Q4 + Q6
    degrees_135 = Q1 + Q9
    # first two if statements should take care of the issue of aspect ratio distortion.
    # That is if a bounding box is so narrow around the syrenge we just assume the 0 or 90 degree 
    # case otherwise we do the summing of quadrants.
    if w * 2 < h: 
        return 0x00
    elif h * 2 < w:
        return 0x5a
    else:
        if degrees_0 > degrees_45 and degrees_0 > degrees_90 and degrees_0 > degrees_135:
            return 0x00
        if degrees_45 > degrees_0 and degrees_45 > degrees_90 and degrees_45 > degrees_135:
            return 0x2d
        if degrees_90 > degrees_0 and degrees_90 > degrees_45 and degrees_90 > degrees_135:
            return 0x5a
        if degrees_135 > degrees_0 and degrees_135 > degrees_90 and degrees_135 > degrees_45:
            return 0x87