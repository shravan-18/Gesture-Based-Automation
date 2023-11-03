import os
import shutil


dir = 'D:\VIT Material\VIT material\Projects\PraySign-PlayMusic\OpenCV\images'
folders = os.listdir(dir)

for folder in folders:
    i = 0
    curr_folder_dir = os.path.join(dir, folder)
    for filename in os.listdir(curr_folder_dir):
        i += 1
        if os.path.isfile(os.path.join(curr_folder_dir, filename)):
            # Define the new name (you can customize the renaming logic)
            new_name = f"image_{i}.jpg"

            # Construct the full paths for the source and destination files
            source_file = os.path.join(curr_folder_dir, filename)
            destination_file = os.path.join(curr_folder_dir, new_name)

            # Rename the file
            os.rename(source_file, destination_file)

print("Renamed images!")