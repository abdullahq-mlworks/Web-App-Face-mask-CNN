## 😷 Face Mask Detection (CNN)
Face Mask Detection is a computer vision project that classifies whether a person is wearing a mask or not using a Convolutional Neural Network (CNN).

---

## 🔎 Overview

* Objective: Detect face mask (Mask / Without Mask) from images.
* Dataset: Custom dataset (images in folders).
* Workflow:

  1. Data Loading (Images from directory using ImageDataGenerator).
  2. Data Preprocessing (Resizing + Normalization).
  3. Model Building (CNN using Keras Sequential API).
  4. Training with validation split.
  5. Evaluation using Accuracy & Loss.
  6. Prediction on new images.

---

## 📂 Project Structure
Face-Mask-Detection-(CNN)/
│
├── Face Mask Detection.ipynb   # Main Notebook
├── model.h5                    # Trained Model
├── requirements.txt            # Dependencies
├── README.md                   # Documentation
│
└── data/
    ├── with_mask/
    └── without_mask/

---

## ⚙️ Installation

Clone repository and install dependencies:
git clone https://github.com/your-username/Face-Mask-Detection-(CNN).git
cd Face-Mask-Detection-(CNN)
pip install -r requirements.txt

---

## 🧾 Dataset

* Type: RGB images
* Size: Resized to 128×128
* Classes: 2
  * with_mask
  * without_mask
* Structure:
data/
    with_mask/
    without_mask/


---

## 🤖 Model

* Algorithm: Convolutional Neural Network (CNN)
* Architecture:
  1. Conv2D (32 filters, ReLU) + MaxPooling
  2. Conv2D (64 filters, ReLU) + MaxPooling
  3. Conv2D (128 filters, ReLU) + MaxPooling
  4. Flatten Layer
  5. Dense (128 neurons, ReLU)
  6. Dense (64 neurons, ReLU)
  7. Output Layer (1 neuron, Sigmoid)
* Compilation:
  * Optimizer: Adam
  * Loss: Binary Crossentropy
  * Metric: Accuracy

---

## 📊 Results
* Model successfully classifies Mask / Without Mask.
* Good accuracy achieved on validation data.
* Stable training with minimal overfitting.

---

## 📈 Output
* Accuracy & Loss values printed after training
* Model predictions on new images:
  * Mask
  * Without Mask

---

## 🧪 Prediction Example
* Load image → Resize (128×128)
* Convert to array → Normalize
* Add batch dimension
* Predict using trained model

---

## 🚀 Future Work
* Real-time detection using OpenCV (webcam)
* Improve accuracy using Data Augmentation
* Use Transfer Learning (MobileNet, VGG16)
* Deploy model (Streamlit / Flask)

---

## 📦 Requirements
tensorflow
numpy
pillow
matplotlib

---