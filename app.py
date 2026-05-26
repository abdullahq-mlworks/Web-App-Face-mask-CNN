# Web app banane ke liye use hoti hai
import streamlit as st 
# Trained ML model (model.h5) load karne ke liye
from tensorflow.keras.models import load_model
# Image ko load + preprocess karne ke lye
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the trained model
model= load_model("model.h5")

# Web page pe heading show hoti hai
st.title("Face Mask Detection")

# Upload file from user
#file_uploader("Upload Image".......):
# "Upload Image" -> Ye UI label (text) hai.Ye user ko screen par show hota hai
upload= st.file_uploader("Upload Image", type= ["jpg", "png", "jpeg"])

# Check image uploaded hai ya nahi
if upload is not None:
    # Load image + resize
    img= image.load_img(upload, target_size= (128, 128))

    # Convert image to array q k ML model sirf numbers samajhta hai
    img_arr= image.img_to_array(img)

    # (128,128,3) -> (1,128,128,3) Model ko batch format chahiye hota hai
    img_arr= np.expand_dims(img_arr, axis= 0)
    img_arr= img_arr/255.0 # Nomalize

    # Prediction (probability -> sigmoid)
    prediction= model.predict(img_arr)

    # User ko original uploaded image show karta hai
    st.image(upload)

    # Final
    if prediction [0][0]<0.5:
        st.write("With Mask")
    else:
        
        st.write("Without Mask")