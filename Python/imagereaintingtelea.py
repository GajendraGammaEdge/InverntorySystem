import cv2 as cv 
import matplotlib.pyplot as plt
import numpy as np 

def  image_repainting(image_path):
    try:
        image = cv.imread(image_path)
        if image is None :
            print("Image is not fount")
            return None
        
        mask = np.zeros(image.shape[:2], dtype=np.uint8)
        mask[50:150, 50:150] = 255
        # blure = cv.GaussianBlur(image, (5,5), 0)
        imagein = cv.inpaint(image, mask , 3 , cv.INPAINT_TELEA)
        cv.imwrite("repainted_imagetelea.png",imagein)
        plt.imshow(imagein)
        plt.show()
    except Exception as e:
        print(f"There is something wrong in the repainting process: {e}")

path= "/home/my/Downloads/Python/iamge11.png"
image_repainting(path)



