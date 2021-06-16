import cv2
import sys

ESC_KEY = 27
TIME_DIFF = 1 #1ms 

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
    cv2.imshow('Preview', frame)
    rval, frame = webcam.read()

    # Wait on user input before closing
    key = cv2.waitKey(1)
    if key == ESC_KEY:
        break

# Destroy the window
cv2.destroyWindow('preview')    
    