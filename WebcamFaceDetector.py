#python3

import cv2
import sys
import random

# Variables to make code cleaner
ESC_KEY = 27
TIME_DIFF = 1 #1ms 
GREEN = (0, 255, 0)

# Get the paths for the image and the cascades you want to pass
casc_path = sys.argv[1] # This should be an XML file

# Create a HAAR cascade
# Loads face cascade into memory => ready to use
face_cascade = cv2.CascadeClassifier(casc_path)

# Open webcam
cv2.namedWindow('Preview') 
webcam = cv2.VideoCapture(0)

# Initialize the webcam
if webcam.isOpened():
    rval, frame = webcam.read()
else:
    rval = False

# Reading data from webcam
while rval:
    # Get the frame itself
    rval, frame = webcam.read()

    # Convert it to grayscale as we don't want it to use colour as a feature
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=4, # Increase this for accuracy
        #flags=cv2.cv.CV_HAAR_SCALE_IMAGE,
        minSize=(30,30)
    )

    # Number of faces
    #print('Number of faces found: ' + str(len(faces)))

    # Draw a rectangle around the faces
    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x+width, y+height), GREEN, 2)

    # Show the frame itself
    cv2.imshow('Preview', frame)

    # Wait on user input before closing
    key = cv2.waitKey(1)
    if key == ESC_KEY:
        break