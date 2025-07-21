import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 


def perspective_transformation(image1):
    try:
        image = cv.imread(image1, cv.IMREAD_GRAYSCALE)
        row, col = image.shape
        sour = np.float32([[100, 100], [400, 100], [100, 400], [400, 400]])
        dest = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
        M = cv.getPerspectiveTransform(sour, dest)
        tran = cv.warpPerspective(image, M , (row, col))
        plt.subplot(121)
        plt.imshow(image, cmap='gray')
        plt.title("Input Image")
        plt.subplot(122)
        plt.imshow(tran, cmap='gray')
        plt.title("Output Image")
        # cv.iwrite("imag", tran)
        plt.show()
    except Exception as e:
        print(f"Error {e}")
        return None


path = "/home/my/Downloads/Python/digitimage.png"
perspective_transformation(path)        