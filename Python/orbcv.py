import cv2 as cv 
import matplotlib.pyplot as plt 
import numpy as np 

image = cv.imread("/home/my/Downloads/Python/Images/image_4.png", cv.IMREAD_GRAYSCALE)

if image is None:
    raise ValueError("Image not found or path is incorrect!")

orb = cv.ORB_create()

kp, dess = orb.detectAndCompute(image, None)

image_with = cv.drawKeypoints(image, kp, None, color=(255, 250, 0), flags=0)


plt.imshow(cv.cvtColor(image_with, cv.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
