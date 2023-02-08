import cv2
import numpy as np
import face_recognition
img_bgr = face_recognition.load_image_file('FaceRecog/images/gfg-200x157.png')
img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
cv2.imshow('bgr', img_bgr)
cv2.imshow('rgb', img_rgb)
cv2.waitKey