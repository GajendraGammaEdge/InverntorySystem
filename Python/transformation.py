import cv2 as cv 
import matplotlib.pyplot as plt 
import numpy as np 


def transformation(image1):
    try :
        image = cv.imread(image1, cv.IMREAD_GRAYSCALE)
        row ,col  = image.shape
        pt1 = np.float32([[50,50], [200,50],[50 , 200]])
        pt2 = np.float32([[10,100],[200,50],[100,250]])
        M = cv.getAffineTransform(pt1, pt2)
        image2 = transformed_image = cv.warpAffine(image, M , (row, col))
        plt.subplot(121) 
        plt.imshow(image)
        plt.title("Input Image")

        plt.subplot(122)
        plt.imshow(image2)
        plt.title("output Image")
        plt.show()
    except Exception as e:
        print(f"Error {e}")
        return None 
        # plt.imshow("input", image )
        # plt.imshow("tran_output", image2)
        plt.show()

path = "/home/my/Downloads/Python/digitimage.png"
transformation(path)        