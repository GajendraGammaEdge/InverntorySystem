import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 

def converting_the_image_hdr(image1):
        try:
                image = [cv.imread(img) for img in image1]
                if any(img is None for img in image):
                        raise ValueError("image not found")
                
                # Resize all images to match the first image size
                height, width = image[0].shape[:2]
                image = [cv.resize(img, (width, height)) for img in image]

                exposure_times = np.array([15.0, 0.25], dtype=np.float32)    
                merge_ger = cv.createMergeDebevec()
                hdr = merge_ger.process(image, times = exposure_times.copy())

                tonemap = cv.createTonemap()
                tonemap_hdr = tonemap.process(hdr)  # << fixed: use HDR, not original image

                merge_ger_unit8 = np.clip(hdr * 255, 0, 255).astype(np.uint8)
                tonemap_unit8 = np.clip(tonemap_hdr * 255, 0, 255).astype(np.uint8)

                cv.imwrite("hdr_image.png", merge_ger_unit8)
                cv.imwrite("tonemap_image1.png", tonemap_unit8)  # << fixed: save correct image

                plt.imshow(merge_ger_unit8)
                plt.figure()
                plt.imshow(tonemap_unit8)
                plt.show()

        except Exception as e:
              print(f"error {e}")
              return None
        

pathlist = ["/home/my/Downloads/Python/Images/image_2.png", "/home/my/Downloads/Python/Images/image_0.png"]
converting_the_image_hdr(pathlist)
