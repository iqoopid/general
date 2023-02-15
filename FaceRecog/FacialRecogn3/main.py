import cv2
import os
import face_recognition

# Load known faces
known_faces_dir = 'known_faces'
known_faces = []
known_names = []
for filename in os.listdir(known_faces_dir):
    image = face_recognition.load_image_file(os.path.join(known_faces_dir, filename))
    encoding = face_recognition.face_encodings(image)[0]
    known_faces.append(encoding)
    known_names.append(os.path.splitext(filename)[0])

# Initialize path for Haar Cascade classifier
cascPath = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascPath)

# Initialize video capture
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    # Convert frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Recognize faces in the frame
    for (x, y, w, h) in faces:
        # Crop face region
        face = frame[y:y+h, x:x+w]

        # Encode face
        encoding = face_recognition.face_encodings(face)

        # Compare face with known faces
        matches = face_recognition.compare_faces(known_faces, encoding)

        # Find best match
        match_index = -1
        min_distance = 1.0
        for i in range(len(matches)):
            if matches[i]:
                distance = face_recognition.face_distance([known_faces[i]], encoding)
                if distance < min_distance:
                    min_distance = distance
                    match_index = i

        # Draw rectangle around face and label with name
        if match_index >= 0:
            name = known_names[match_index]
        else:
            name = 'Unknown'
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        
    # Display the resulting frame
    cv2.imshow('Face recognition', frame)
    
    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close windows
cap.release()
cv2.destroyAllWindows()
