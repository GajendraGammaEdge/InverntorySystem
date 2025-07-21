import cv2 as cv 
import matplotlib.pyplot as plt 
import numpy as np

path = "/home/my/Downloads/Python/digitimage.png"

image = cv.imread(path, cv.IMREAD_GRAYSCALE)
kernel = np.ones((1, 3), np.uint8)

erosion = cv.erode(image, kernel, iterations=1)
dilation = cv.dilate(image, kernel, iterations=1)

titles = ["Erosion", "Dilation"]
images = [erosion, dilation]

for i in range(len(images)):
    plt.subplot(1, 2, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.tight_layout()
plt.show()
