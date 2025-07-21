from spire.pdf.common import *
from spire.pdf import *
import os 
# import pytessaractfile

pdf_path = "/home/my/Downloads/Python/guru.pdf"
output_folder = "/home/my/Downloads/Python/Images"

doc = PdfDocument()
doc.LoadFromFile(pdf_path)
os.makedirs(output_folder, exist_ok=True)

def extract_image_from_pdf(doc):
    '''Extracts image from the pdf file and also extracting the text from the image using'''
    imageHelper = PdfImageHelper()
    index = 0

    for i in range(doc.Pages.Count):
        page = doc.Pages.get_Item(i)
        imageInfos = imageHelper.GetImagesInfo(page)

        if not imageInfos:
            print(f"No image found on page {i + 1}")
            continue

        for imageInfo in imageInfos:
            image = imageInfo.Image
            
            image_filename = os.path.join(output_folder, f"image_{index}.png")
            # text = pytessaractfile.extract_text_from_image(image)
            # if text:
            #     print(f"Extracted text from image_{index}:{text}")
            #     return text
            # else:
            #     print(f"No text present in image_{index}")
            image.Save(image_filename)
            print(f" Image saved as: image_{index}.png")
            index += 1

extract_image_from_pdf(doc)
doc.Dispose()
print("\nImage extraction completed.")
