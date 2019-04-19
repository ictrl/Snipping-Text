import cv2 , os
import pytesseract
import numpy as np
from PIL import Image
from PIL import ImageGrab

# Path of Tesseract-OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

Screenshot = ImageGrab.grabclipboard()

NpImg = np.array(Screenshot)

def getContent(srcImg):

    img = cv2.cvtColor(srcImg, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite("finalPic.png", img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open("finalPic.png"))

    # Remove FianlPic
    os.remove("finalPic.png")
    return result

f= open("Content.txt","w+")
f.write(getContent(NpImg))
os.startfile("Content.txt")
