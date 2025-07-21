import cv2 as cv 
import numpy as np 

def digit_classification(path):
    try:
        
        image = cv.imread(path, cv.IMREAD_GRAYSCALE)
        if image is None:
            print("Image not found:", path)
            return
        image = cv.resize(image, (2000, 1000))

        cells = [np.hsplit(row, 100) for row in np.vsplit(image, 50)]
        x = np.array(cells)

        x_train = x[:, :50].reshape(-1, 400).astype(np.float32)  
        x_test = x[:, 50:100].reshape(-1, 400).astype(np.float32) 

        k = np.arange(10)
        y_train_labels = np.repeat(k, 250)[:, np.newaxis]
        y_test_labels = y_train_labels.copy()

        knnn = cv.ml.KNearest_create()  
        knnn.train(x_train, cv.ml.ROW_SAMPLE, y_train_labels)

        ret, results, neighbours, dist = knnn.findNearest(x_test, k=5)
        
        accuracy = np.mean(results == y_test_labels)
        print(f"Accuracy: {accuracy * 100:.2f}%")
    except Exception as e:
        print(f"Error: {e}")     
        return None  

path = "/home/my/Downloads/Python/digitimage.png"
digit_classification(path)
