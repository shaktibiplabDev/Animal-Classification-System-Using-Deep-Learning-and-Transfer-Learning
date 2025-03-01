# Animal Classification System Using Deep Learning

## Overview
This project focuses on developing an **Animal Classification System** using deep learning and transfer learning techniques. The system is capable of identifying **15 different animal species** from images with high accuracy and efficiency. It leverages the **MobileNetV2** architecture for classification and features a user-friendly **drag-and-drop GUI** for real-time predictions.

## Features
- **Real-time Image Classification**
- **Drag-and-Drop Interface**
- **Confidence-Based Feedback**
- **High Accuracy (95.2%)**
- **Lightweight and Efficient Model**

## Technologies Used
- **Deep Learning Framework**: TensorFlow & Keras
- **Model Architecture**: MobileNetV2 (pre-trained on ImageNet)
- **Programming Language**: Python
- **GUI Development**: Tkinter & TkinterDnD
- **Data Augmentation**: Rotation, Zooming, Flipping

## Dataset
The dataset consists of **15 classes** of animals:
- **Bear**
- **Bird**
- **Cat**
- **Cow**
- **Deer**
- **Dog**
- **Dolphin**
- **Elephant**
- **Giraffe**
- **Horse**
- **Kangaroo**
- **Lion**
- **Panda**
- **Tiger**
- **Zebra**

Each image is resized to **224x224x3** to match MobileNetV2's input requirements.

## Model Training
- **Optimizer**: Adam
- **Learning Rate**: 0.0001
- **Epochs**: 20
- **Validation Accuracy**: 95.2%
- **Confidence Threshold**: 70% (If below, returns "Sorry, I am unable to detect that.")

## Installation
### Prerequisites
Ensure you have Python installed. Recommended version: **Python 3.8+**

### Install Dependencies
```bash
pip install tensorflow keras opencv-python pillow numpy tkinterdnd2
```

### Clone the Repository
```bash
git clone https://github.com/shaktibiplabDev/Animal-Classification-System-Using-Deep-Learning-and-Transfer-Learning animal-classification
cd animal-classification
```

### Run the Application
```bash
python classify.py
```

## Usage
1. **Launch the application** using the command above.
2. **Drag and drop an image** onto the interface.
3. **View the classification result** and confidence score.
4. If confidence is below **70%**, the system responds with: *"Sorry, I am unable to detect that."*

## Applications
- **Wildlife Monitoring**: Classify animals in camera trap images.
- **Education**: Interactive tool for learning about animal species.
- **Conservation**: Helps track endangered species.

## Future Improvements
- Expand dataset for better generalization.
- Improve model robustness against non-animal images.
- Support additional animal species.

## References
1. Howard, A. G., et al. *MobileNetV2: Inverted Residuals and Linear Bottlenecks.* arXiv preprint arXiv:1801.04381 (2018).
2. Chollet, F. *Deep Learning with Python.* Manning Publications (2017).
3. TensorFlow Documentation: [https://www.tensorflow.org/](https://www.tensorflow.org/)

---
Developed by **Shakti Biplab**

