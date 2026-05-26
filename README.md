# Face Mask Detection Web Application
A Deep Learning web application built with Convolutional Neural Networks (CNN) and TensorFlow to detect whether a person is wearing a face mask or not. The user interface is developed using Streamlit for quick and efficient local and cloud deployment.

---

## Features
* Image Upload: Supports `.jpg`, `.jpeg`, and `.png` image formats.
* Deep Learning Pipeline: Preprocesses and normalizes images to `128x128` pixels before feeding them into the trained CNN model.
* Real-time Prediction: Uses a binary classification model (Sigmoid activation) to output predictions instantly.
* Minimalist UI: Clean and simple layout for seamless user experience.

---

## Tech Stack
* Language: Python
* Framework: Streamlit
* Deep Learning Library: TensorFlow / Keras
* Data Processing: NumPy

---

## 📁 Repository Structure
* `app.py` - The main Streamlit web application code.
* `model.h5` - The pre-trained Convolutional Neural Network (CNN) model.
* `requirements.txt` - List of required Python libraries for deployment.
* `Face Mask Detection.ipynb` - The Jupyter Notebook containing model training and evaluation code.

---

## ⚙️ How to Run Locally
Clone the repository:
git clone https://github.com/abdullahq-mlworks/Web-App-Face-mask-CNN.git
cd Web-App-Face-mask-CNN

---

## Create and Activate Virtual Environment:
python -m venv ten_env

---

## On Windows:
ten_env\Scripts\activate

---

## Install Dependencies:
pip install -r requirements.txt

---

## Run the Application:
streamlit run app.py