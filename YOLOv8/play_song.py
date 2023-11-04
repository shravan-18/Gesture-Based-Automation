import os
import random

# Specify the directory containing the songs
directory = "D:\VIT Material\VIT material\Projects\PraySign-PlayMusic\YOLO\songs"

# Get a list of all files in the directory
files = os.listdir(directory)

# Filter the list to include only mp3 files
mp3_files = [file for file in files if file.endswith('.mp3')]

# Select a random file from the list
random_file = random.choice(mp3_files)

# Construct the full path to the file
full_path = os.path.join(directory, random_file)

# Open the file with the default application
os.startfile(full_path)
