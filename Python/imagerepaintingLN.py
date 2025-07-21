import numpy as np 
import cv2 as cv 
import matplotlib.pyplot as plt

def covert_repainting(image2):
    try:
        imag = cv.imread(image2)
        if imag is None:
            print("Image not fount")
            return None
        
        mask = np.zeros(imag.shape[:2], dtype=np.uint8)
        mask[50:150 , 50:150] = 255
        imagin = cv.inpaint(imag, mask, 3 , cv.INPAINT_NS)
        cv.imwrite("Ns.png", imagin)
        plt.imshow(imagin)
        plt.show()
    except Exception as e :
        print(f"Ther is something wrong {e}")
        return None
    
path = "/home/my/Downloads/Python/iamge11.png"
covert_repainting(path)   