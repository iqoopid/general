'''
Capture multiple Faces from multiple users to be stored on a DataBase (dataset directory)

'''

import cv2

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

eye_detector = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_detector = cv2.CascadeClassifier('haarcascade_smile.xml')
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id
face_id = input('\n Enter user id and press <return> :  ')

print("\n [INFO] Initializing face capture. Look at the camera and wait ...")
# Initialize individual sampling face count
count = 0

while(True):

    ret, img = cam.read()
    # img = cv2.flip(img, -1) # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5) # 1.3 is the scale factor, 
    # which determines how much the image is resized at each scale. 
    # In this case, the image is resized by 30% at each step.

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w+10,y+h+10), (255,0,0), 2)     
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('Capture', img)

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 100: # Take 100 face sample and stop video
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program...")
cam.release()
cv2.destroyAllWindows()
