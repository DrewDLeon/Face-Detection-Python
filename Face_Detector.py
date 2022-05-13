#OPENCV es Computer Vision
import cv2
#IMAGE DETECTION
"""
from random import randrange as rd

#Cargamos el dataframe entrenado de caras para hacer uso de el
trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#Leemos la imagen a identificar
img = cv2.imread('gignac.jpg')

#Convertimos la imagen a escala de grises para reducir la cantidad de numeros
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detectar Rostros
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
print(face_coordinates)

#Dibujar los rectangulos
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (rd(256), rd(256), rd(256)), 2)

#Mostrar la imagen en pantalla
cv2.imshow('Deteccion facial', img)
cv2.waitKey() ##WaitKey es utilizado para retener la imagen abierta
"""


#VIDEO DETECTION
webcam = cv2.VideoCapture(0)
#Cargamos el dataframe entrenado de caras para hacer uso de el
trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#Mantener la captura de frames
while True:

    ##Leer frames
    succesful_frame_read, frame = webcam.read()

    #Transformamos a grayscale
    grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Detectar las coordenadas
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_frame)

    #Dibujar los rectangulos
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    #Mostramos la webcam
    cv2.imshow('Deteccion facial', frame)
    key = cv2.waitKey(1)

    #Parar si presionamos la tecla Q
    if key == 81 or key == 113:
        break

###Webcam release
webcam.release()


#Se lee si funciono o no
print("Code Completed")