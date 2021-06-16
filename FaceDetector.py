#python3

import cv2
import sys
import random

# Get the paths for the image and the cascades you want to pass
image_path = sys.argv[1]
casc_path = sys.argv[2] # This should be an XML file

# Create a HAAR cascade
# Loads face cascade into memory => ready to use
face_cascade = cv2.CascadeClassifier(casc_path)

# Actually read the image and convert to greyscale 
# i.e. remove colour as a feature
img = cv2.imread(image_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=4, # Increase this for accuracy
    #flags=cv2.cv.CV_HAAR_SCALE_IMAGE,
    minSize=(30,30)
)

# Number of faces
print('Number of faces found: ' + str(len(faces)))

# Draw a rectangle around the faces
for (x, y, width, height) in faces:
    colour = tuple([random.randint(0,255) for _ in range(3)])
    cv2.rectangle(img, (x, y), (x+width, y+height), colour, 2)

# Actually show the new image w/ detected faces
cv2.imshow('Here are the detected faces', img)

# Wait for user input till to terminate the program
cv2.waitKey(0)