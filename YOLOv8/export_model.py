import cv2
from ultralytics import YOLO
import time
import numpy as np

model_path = "D:\VIT Material\VIT material\Projects\PraySign-PlayMusic\\runs\detect\\train-final\weights\last.pt"
model = YOLO(model_path)

results = model.export(format="onnx", opset=12)  # export the model to ONNX format
print("Model exported to ONNX format.")
