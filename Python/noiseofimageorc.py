#using the open cv to reduce the noise in the image 
import cv2 as cv 
import matplotlib.pyplot as plt 

def reduce_image_noise(imag1):

    img = cv.imread(imag1, cv.IMREAD_GRAYSCALE)
    if imag1 is None:
        raise ValueError("imagenot found")
    
    noisey = cv.fastNlMeansDenoising(img, None , 10,7  , 21)
    cv.imwrite("noisey_image.png", noisey)
    plt.imshow(cv.cvtColor(noisey, cv.COLOR_BGR2RGB))
    plt.show()

path = "/home/my/Downloads/Python/Images/image_1.png"
reduce_image_noise(path)   