import cv2
import numpy as np
from PIL import Image
import database as dtb
from pytesseract import pytesseract
from datetime import datetime, date, time, timedelta


def tesseract():
    # path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    path_to_tesseract = r'D:\Programs\Tesseract\tesseract.exe'
    image_path = 'test.jpg'
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(Image.open(image_path),config='--psm 11').strip()
    now = date.today()
    nowdate = now.strftime('%d/%m/%Y')
    dtb.insertrow(text,nowdate)
    dtb.exportcv()
    print(text[:-1])

cap = cv2.VideoCapture(0)
amarilloBajo = np.array([15,100,20],np.uint8)
amarilloAlto = np.array([45,255,255],np.uint8)

while True:
  ret, frame = cap.read()
  if ret==True:
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frameHSV, amarilloBajo,amarilloAlto)

    cv2.imshow('frame', frame)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("res", res)
    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)


    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('test.jpg',  cv2.blur(gray,(3,3))  )
        break
cap.release()
cv2.destroyAllWindows()
tesseract()