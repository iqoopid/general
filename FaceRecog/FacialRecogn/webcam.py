import cv2
import numpy as np
import face_recognition

imgElon = face_recognition.load_image_file('Images/elon1.jpg')
imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)

faceloc = face_recognition.face_locations(imgElon)[0]
encodeElon = face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon,(faceloc[3], faceloc[0], faceloc[1], faceloc[2]),(255,0,0),3)

print(faceloc)

cv2.imshow('Elon Musk', imgElon)