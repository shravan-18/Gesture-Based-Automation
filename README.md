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
- High accuracy and performance, but computationally heavy.

### TinyYOLO
- Lightweight model but did not perform as well as YOLOv8 in our tests.

### OpenCV
- Used primarily for basic image processing tasks. 

### TensorFlow
- Powerful but computationally intensive, suitable for real-time processing on Raspberry Pi - hence chosen.

The results of the model comparisons and training performance can be found in the Results folder. Below is a summary graph of the training results for YOLOv8:
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
3. **Setup Raspberry Pi Camera**
   - Enable the camera interface using `sudo raspi-config`.
   - Test the camera with `raspistill -o image.jpg`.
     
## Download and Prepare Models
1. **Main Model Configuration**
   - The main model configuration can be found in the following directory:
     [Main Model Configuration](https://github.com/shravan-18/Gesture-Based-Automation/tree/main/TensorFlow/workspace/training_demo/models/my_ssd_mobilenet_v2_fpnlite)
   - This directory contains configuration files and scripts necessary to set up the SSD MobileNet V2 FPNLite model for training.

2. **Final Model File Weights**
   - The final trained model weights are available in this directory:
     [Final Model File Weights](https://github.com/shravan-18/Gesture-Based-Automation/tree/main/TensorFlow/workspace/training_demo/exported-models/my_mobilenet_model)
   - Download the model weights and place them in the appropriate directory as specified in your setup instructions.

3. **Preprocessing Scripts**
   - The preprocessing scripts, which are essential for preparing the dataset for training and evaluation, are located here:
     [Preprocessing Scripts](https://github.com/shravan-18/Gesture-Based-Automation/tree/main/TensorFlow/scripts/preprocessing)
   - These scripts include functions for data augmentation, normalization, and other preprocessing tasks required for optimal model performance.

## Contributing
We welcome contributions to enhance the functionality and performance of this project. Please follow these guidelines for contributing:

1. **Fork the Repository**
   - Click the 'Fork' button on the top right of the repository page.

2. **Clone the Forked Repository**
   ```bash
   git clone https://github.com/your-username/Gesture-Based-Automation.git
   cd Gesture-Based-Automation```
3. **Create a branch**
   ```bash
   git checkout -b feature-name```
4. **Make your changes**
   Implement your changes and make sure they are properly tested.
5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Description of your changes"```
6. **Push to your Fork**
   ```bash
   git push origin feature-name```
7. **Create a Pull Request**
   - Go to the original repository and click the 'New Pull Request' button.
   - Provide a clear and descriptive title and description of your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements
- **Vellore Institute of Technology**: For their support and opportunity.
- - **Aravintakshan S A**: For their contribution to this repository.
- **Open-Source Communities**: Developers of YOLO, TensorFlow, and OpenCV for their tools and resources.

For more details, visit our [GitHub repository](https://github.com/shravan-18/Gesture-Based-Automation).

