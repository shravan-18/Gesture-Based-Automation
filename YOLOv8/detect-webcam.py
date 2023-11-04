from ultralytics import YOLO
from PIL import Image
import cv2
import os
import random

# pip install mpyg321
from mpyg321.mpyg321 import MPyg321Player

model = YOLO("YOLO\\runs\detect\\train-large-2\weights\last.pt")
# print(f"Model: {model}")

# open a video file or start a video stream
cap = cv2.VideoCapture(0)  # replace with 0 for webcam

music_dir = "music directory"
songs = os.listdir(music_dir)

while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Run inference on the current frame
    results = model(frame, conf=0.8)  # results list
    print(f"Results: {results}")
    for r in results:
        # print(f"r: {r}")
        frame = r.plot()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Extract the classes of the detected objects
    classes = [result.boxes.cls for result in results]

    if classes:
        player = MPyg321Player()
        song = random.choice(songs)
        song_path = os.path.join(music_dir, song)
        player.play_song(song_path)

    
    # Press 'q' on keyboard to  exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object and destroy all windows
cap.release()
cv2.destroyAllWindows()