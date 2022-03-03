import cv2
import numpy as np
from PIL import Image
from pytesseract import pytesseract

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
     _,image = camera.read()

     hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
     # Threshold of blue in HSV space
     lower_blue = np.array([60, 35, 140])
     upper_blue = np.array([180, 255, 255])
     mask = cv2.inRange(hsv, lower_blue, upper_blue) 

     cv2.imshow('image',image)
     cv2.imshow('mask', mask)
     if cv2.waitKey(1)& 0xFF==ord('s'):
         cv2.imwrite('test.jpg',image)
         break

camera.release()
cv2.destroyAllWindows()

def tesseract():
    path_to_tesseract = r'D:\Programs\Tesseract\tesseract.exe'
    image_path = 'test.jpg'
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(Image.open(image_path))
    print(text[:-1])

tesseract()