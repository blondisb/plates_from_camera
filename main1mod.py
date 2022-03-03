import cv2
import numpy as np
from PIL import Image
import database as dbs
from pytesseract import pytesseract

def tesseract():
    path_to_tesseract = r'D:\Programs\Tesseract\tesseract.exe'
    image_path = 'test.jpg'
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(Image.open(image_path))
    print(text[:-1])

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
amarilloBajo = np.array([15,100,20],np.uint8)
amarilloAlto = np.array([45,255,255],np.uint8)

while True:
    #  _,image = camera.read()
     ret, frame = camera.read()

     if ret == True:
         frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
         mask = cv2.inRange(frameHSV, amarilloBajo,amarilloAlto)

        # hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        # # Threshold of blue in HSV space
        # lower_blue = np.array([60, 35, 140])
        # upper_blue = np.array([180, 255, 255])
        # mask = cv2.inRange(hsv, lower_blue, upper_blue) 

         cv2.imshow('frame',frame)
         res = cv2.bitwise_and(frame, frame, mask=mask)
         cv2.imshow("res", res)
         gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
   
         if cv2.waitKey(1)& 0xFF==ord('s'):
            cv2.imwrite('test.jpg',cv2.blur(gray,(3,3)))
            break

camera.release()
cv2.destroyAllWindows()
tesseract()