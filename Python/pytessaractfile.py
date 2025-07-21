import pytesseract
from PIL import  Image


def extract_text_from_image():
    """Extracting the text from the image using the pytesseact library."""
    try:
        #opening the image using PIL
        image  = Image.open("/home/my/Downloads/Python/Images/image_1.png")
        #usigng the pytesseract 
        resize_image = image.resize((image.width*3, image.height*3))
        image_text = pytesseract.image_to_string(resize_image, lang= 'eng')
        return image_text
    except Exception as e:
        print(f"An error occurred while extracting text from the image: {e}")
        return None 

te = extract_text_from_image()
print(te)
