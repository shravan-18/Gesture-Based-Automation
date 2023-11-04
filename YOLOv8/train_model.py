from ultralytics import YOLO

# Create model from scratch
model = YOLO('yolov8m.pt')

# Train the model
model.train(data='D:\VIT Material\VIT material\Projects\PraySign-PlayMusic\config.yaml', epochs=100)