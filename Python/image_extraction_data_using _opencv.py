import cv2 as cv

def extract_image(image_path):
    '''Performing the image extraction using OpenCV'''

    try:
        image = cv.imread(image_path)
        if image is None:
            print("Image not found or failed to load.")
            return None
        else:
           
            cv.imwrite("image12.png", image)
            return image
    except Exception as e:
        print(f"Image extraction failed: {e}")
        return None


path = "/home/my/Downloads/Python/Images/image_4.png"
image = extract_image(path)

if image is not None:
    print("Image shape:", image.shape)
else:
    print("No image returned.")
