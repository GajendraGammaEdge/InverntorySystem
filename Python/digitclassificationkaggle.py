import kagglehub
import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 


path = kagglehub.dataset_download("jcprogjava/handwritten-digits-dataset-not-in-mnist")
if path is not None:
    print(f"Dataset downloaded to :{path}")

print("Path to dataset files:", path)

def digit_classification():
      img = cv.imread(path , cv.IMREAD_GRAYSCALE)
      if img is None :
           print("Image not found")
           return None
      
