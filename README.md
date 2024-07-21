# Gesture-Based-Automation
![Machine Learning](https://img.shields.io/badge/Raspberry_Pi-Edge_Computing-red.svg)
![Deep Learning](https://img.shields.io/badge/Deep_Learning-Computer_Vision-green.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)

This project leverages the power of Raspberry Pi 4 and computer vision models to analyze gestures made by individuals in front of a Pi camera. The system plays audio media based on the detected gestures, aimed at improving education and respect among children in rural schools. The project was developed for the consultancy Innovative Implements Pvt Ltd, commissioned by the State Government of Tamil Nadu.

## Table of Contents
- [Overview](#overview)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Model Comparison](#model-comparison)
- [Setup Instructions](#setup-instructions)
- [Training](#training)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Overview
The project employs four different models: YOLOv8, TinyYOLO, OpenCV, and TensorFlow, to identify the best performing model for gesture recognition. The final implementation uses YOLOv8 due to its superior performance. The audio content played is confidential, focusing on enhancing educational experiences and promoting respectful behavior in students.

## Hardware Requirements
- Raspberry Pi 4
- Pi Camera
- MicroSD card (32GB or higher recommended)
- Power supply for Raspberry Pi
- Speaker or audio output device

## Software Requirements
- Raspberry Pi OS
- Python 3.7 or higher
- YOLOv8
- TinyYOLO
- OpenCV
- TensorFlow
- Required Python packages (detailed in `requirements.txt`)

## Model Comparison
### YOLOv8
- Final chosen model due to its high accuracy and performance.

### TinyYOLO
- Lightweight model but did not perform as well as YOLOv8 in our tests.

### OpenCV
- Used primarily for basic image processing tasks. 

### TensorFlow
- Powerful but computationally intensive, less suitable for real-time processing on Raspberry Pi.

![Training Results](https://github.com/shravan-18/Gesture-Based-Automation/blob/main/YOLOv8/Results/results.png)

## Setup Instructions
1. **Clone the Repository**
   ```bash
   git clone https://github.com/shravan-18/Gesture-Based-Automation.git
   cd Gesture-Based-Automation```
2. **Install Dependencies**
   ```bash
   sudo apt-get update
   sudo apt-get upgrade
   sudo apt-get install python3-pip
   pip3 install -r requirements.txt```
