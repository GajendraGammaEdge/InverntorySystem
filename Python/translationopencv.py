import cv2 as cv 
import numpy as np 


def  image_translation(imag1):
    try:
        image =  cv.imread(imag1 , cv.IMREAD_GRAYSCALE)
        
        row , col = image.shape
        M = np.float32([[1,0,50],[0,1,80]])
        translation_image = cv.warpAffine(image ,M ,(row, col))
        cv.imshow('img', translation_image)
        cv.waitKey(0)
        cv.destroyAllWindows()
    except Exception as e:
        print(f"error {e}")
        return None 
    
path  =    "/home/my/Downloads/Python/digitimage.png"
image_translation(path) 