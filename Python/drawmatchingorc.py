import cv2 as cv 
import matplotlib.pyplot as plt 
import numpy as np 

def draw_matching_the_object(image1, image2):

    image1 = cv.imread(image1, cv.IMREAD_GRAYSCALE)
    image2 = cv.imread(image2 ,cv.IMREAD_GRAYSCALE)
    orb = cv.ORB_create()

    kp1 = orb.detect(image1, None)
    kp2 = orb.detect(image2 , None)

    kp1, des = orb.compute(image1, kp1)
    kp2 , de2 = orb.compute(image2, kp2)

    matcher = cv.BFMatcher(cv.NORM_HAMMING, crossCheck = True)
    matcher = matcher.match(des, de2)

    matcher = sorted(matcher, key  = lambda x: x.distance)
    imag3 =  cv.drawMatches(image1, kp1, image2, kp2, matcher[:10], None, flags =cv.DrawMatchesFlags_DEFAULT)
    plt.imshow(imag3)
    plt.show()



path1 = "/home/my/Downloads/Python/Images/image_0.png"
path2 = "/home/my/Downloads/Python/Images/image_2.png"   

draw_matching_the_object(path1, path2)