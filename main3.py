import cv2
import numpy as np
from PIL import Image
import database as dtb
import reg_exp as rxp
from pytesseract import pytesseract
from datetime import datetime, date, time, timedelta


texto=""
def tesseract(imagen):
    # path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    path_to_tesseract = r'D:\Programs\Tesseract\tesseract.exe'    
    image_path = 'test.jpg'
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(imagen,config='--psm 11')
    print(text[:-1])
    return text[:-1]

cap = cv2.VideoCapture(0)
amarilloBajo = np.array([15,100,20],np.uint8)
amarilloAlto = np.array([45,255,255],np.uint8)

while True:
  ret, frame = cap.read()
  if ret==True:
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frameHSV, amarilloBajo,amarilloAlto)

    #cv2.imshow('frame', frame)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    #cv2.imshow("res", res)
    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    gray = cv2.blur(gray,(3,3))

    canny = cv2.Canny(gray, 10, 150)
    #_, canny = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
    canny = cv2.dilate(canny, None, iterations=1)
    canny = cv2.erode(canny, None, iterations=1)
    
    cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #con = cv2.drawContours(gray, cnts, -1, (0,255,0), 2)

    for c in cnts:

        area = cv2.contourArea(c)
        epsilon = 0.09*cv2.arcLength(c,True)
        approx = cv2.approxPolyDP(c,epsilon,True)
        #print(len(approx))
        x,y,w,h = cv2.boundingRect(approx)
        
        if len(approx)==4 and area > 5000:
          aspect_ratio = float(w)/h
          if aspect_ratio > 2.1:
              print('aspect_ratio= ', aspect_ratio)
              placa = gray[y-51:y+h+51,x-51:x+w+51]
              texto = tesseract( cv2.blur(placa,(3,3)))
              texto = rxp.platesformat(texto)
              now = date.today()
              nowdate = now.strftime('%d/%m/%Y')
              dtb.insertrow(texto,nowdate)
            #   dtb.exportcv()
              cv2.imwrite('test.png',placa)
            
              cv2.imshow('PLACA',placa)
              cv2.moveWindow('PLACA',780,10)
              cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
              cv2.putText(frame,texto,(x-20,y-10),1,2.2,(0,255,0),3)


    cv2.imshow("gray",frame)
    
    
    #cv2.imwrite('test.jpg',  canny  )
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
cap.release()
cv2.destroyAllWindows()




