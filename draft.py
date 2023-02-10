import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
import h5py

# import subprocess
# import sys

# def install(package):
#     subprocess.check_call([sys.executable, "-m", "pip", "install", package])
#
# # install(os-sys)
# install(h5py)

import tensorflow as tf
import os

title = st.container()
dataset = st.container()
user_interaction = st.container()
model = st.container()
junk = st.container()

directory = os.getcwd()
path_type = os.path.join(directory+"/Trained_for_Outfits3.h5")
path_color = os.path.join(directory+"/Trained_for_Outfits4.h5")
model_type = tf.keras.models.load_model(path_type)
model_color = tf.keras.models.load_model(path_color)
st.write(path)

@st.cache
def get_data(filename):
  data = pd.read_csv(filename)
  return data

col1,col2,col3,col4,col5 = st.columns(5)

if "photo" not in st.session_state:
    st.session_state["photo"]="not done"

def change_photo_state():
    st.session_state["photo"]="done"
    
with col3:
  with title:
    st.title("Outfit Recommender")

with col1:
    st.title("Introduction")
   
st.write("This project aims to develop an outfit recommendation system using deep learning techniques. The system will take an image from the user as input and suggest a suitable outfit for them. The model will learn to recognize patterns and features in the images, allowing it to make accurate recommendations.")


st.subheader("*Important*")
st.write("Please note the following before uploading your item")
st.markdown("* Rule 1")
st.markdown("* Rule 2")
item = st.file_uploader("Please upload a clothing item",on_change=change_photo_state)
st.write(type(item))
camera_pic = st.camera_input("Please take a photo!",on_change=change_photo_state)
progress_bar = st.progress(0) 
if st.session_state["photo"]=="done":
    for perc_completed in range(100):
      time.sleep(0.01)
      progress_bar.progress(perc_completed+1)
    st.success("Photo uploaded successfully")
    st.metric(label="Temperature", value="60 C",delta="3 C")
    with st.expander("Click to read more"):
      st.write("here is your photo!")
      if item is None:
        st.image(camera_pic)
      else:
        st.image(item)
st.write(camera_pic)
st.download_button(
    label="Download image",
    data=camera_pic,
    file_name= "test_image.jpg"
)
st.write(type(camera_pic))
if camera_pic is not None:
    # To read image file buffer as a PIL Image:
    img = Image.open(camera_pic)

    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Check the type of img_array:
    # Should output: <class 'numpy.ndarray'>
    st.write(type(img_array))

    # Check the shape of img_array:
    # Should output shape: (height, width, channels)
    st.write(f"PIL shape: {img_array.shape}")
    
    # Convert image to required size:
    img = camera_pic.resize((80,60))
    st.write(img)
