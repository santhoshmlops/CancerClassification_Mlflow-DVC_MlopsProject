import cv2
import os
import numpy as np
import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image



# Load the pre-trained model
#model = tf.keras.models.load_model(os.path.join("artifacts","training", "model.h5"))
model = tf.keras.models.load_model(os.path.join("model", "model.h5"))


# Define a dictionary mapping class indices to class names
map_dict = {0: 'Adenocarcinoma Cancer',
            1: 'Normal'}

# Main function to define the Streamlit application
def main():
    # Set the title of the Streamlit app
    st.title("Chest Cancer Image Classifier - VGG16 Model ")
    st.write("Upload an image for classification ")  # Write a description for the app
    
    # Create a file uploader component for users to upload images
    uploaded_file = st.file_uploader("Choose a image file", type=["jpg", "jpeg", "png"])

    # If an image is uploaded
    if uploaded_file is not None:
        # Convert the file to an OpenCV image
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
        resized = cv2.resize(opencv_image, (224, 224))  # Resize the image to the required input size
        
        # Display the uploaded image
        st.image(opencv_image, channels="RGB")

        # Preprocess the image
        resized = tf.keras.applications.mobilenet.preprocess_input(resized)
        img_reshape = resized[np.newaxis,...]

        # Create a button to generate prediction
        Genrate_pred = st.button("Generate Prediction")    
        if Genrate_pred:
            # Predict the label for the image
            prediction = model.predict(img_reshape).argmax()
            # Display the predicted label
            st.title("Predicted Label for the image : {}".format(map_dict[prediction]))


if __name__ == '__main__':
    main()