import cv2
import os
import pygame
import random

song_dir = "D:\VIT Material\VIT material\Projects\PraySign-PlayMusic\OpenCV\songs"

# We point OpenCV's CascadeClassifier function to where our 
# classifier (XML file format) is stored
face_classifier = cv2.CascadeClassifier("D:\VIT Material\VIT material\Projects\PraySign-PlayMusic\OpenCV\cascade.xml")

def face_detector(img, size=0.5):
    # Convert image to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.1, 5)
    if faces is ():
        return img
    
    for (x,y,w,h) in faces:

        x = x - 50
        w = w + 50
        y = y - 50
        h = h + 50
        print(x, w, y, h)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        # pygame.mixer.init()
        # # Specify the path to your song file
        # songs = os.listdir(song_dir)
        # random_song = random.choice(songs)
        # song_file = os.path.join(song_dir, random_song)

        # # Load the song
        # pygame.mixer.music.load(song_file)
        # # Play the song
        # pygame.mixer.music.play()

        # while pygame.mixer.music.get_busy():
        #     continue
        
        
    roi_color = cv2.flip(roi_color,1)
    return roi_color

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1920)

while True:

    ret, frame = cap.read()
    cv2.imshow('Our Face Extractor', face_detector(frame))
    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break
        
cap.release()
cv2.destroyAllWindows()  
