'''
Real Time Face Recogition

'''


import cv2
# import attendance

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_DUPLEX

#initiate id counter
id = 0

# names related to ids: example ==> : id=1,  etc
names = ['Ciril', 'Vishnu', 'Manohar', 'Abin'] 

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:

    ret, img = cam.read()
    # img = cv2.flip(img, -1) # Flip vertically
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.1, # scaleFactor is the factor by which the image is resized at each scale. A value of 1.2 means that the image is scaled by 20% at each step.
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        # The recognizer.predict (), will take as a parameter a captured portion 
        # of the face to be analyzed and will return its probable owner, indicating 
        # its id and how much confidence the recognizer is in relation with this match.
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        # Check if confidence is less than 100 ==> "0" is perfect match 
        if (confidence < 100):
            Id = names[id-1]
            confidence = confidence - 20
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            Id = "Unknown"
            confidence = "  {0}%".format(round(100 - confidence))
        
        cv2.putText(img, str(Id), (x+5,y-5), font, 1, (0,0,0), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
        
        # attendance.record(id, Id)

    cv2.imshow('Face Recognition',img)

   

    # waitKey() method will show the image for 10 milliseconds 
    # before it automatically closes.
    # The & 0xff is a bitwise AND operation that extracts 
    # the least significant 8 bits of the result, 
    # effectively masking all the other bits.
    k = cv2.waitKey(10) & 0xff 
    if k == 27: # Press 'ESC' for exiting video
        break

# Do cleanup
print("\n [INFO] Exiting Program")
cam.release()
cv2.destroyAllWindows()