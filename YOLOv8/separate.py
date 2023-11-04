import os
import shutil

curr_dir = "D:\VIT Material\VIT material\Projects\PraySign-PlayMusic\Data"
images = os.path.join(curr_dir, "images")
labels = os.path.join(curr_dir, "labels")

new_img_path = os.path.join(curr_dir, "imgs")
new_label_path = os.path.join(curr_dir, "lbls")

for label in os.listdir(labels):
    for image in os.listdir(images):
        if label.split('.')[0]==image.split('.')[0]:
            old_label_path = os.path.join(labels, label)
            new_label = os.path.join(new_label_path, label)
            old_image_path = os.path.join(images, image)
            new_img = os.path.join(new_img_path, image)
            shutil.move(old_label_path, new_label)
            shutil.move(old_image_path, new_img)