"""This is a test for streamlit"""
import streamlit as st
import numpy as np
import pandas as pd

title = st.container()
dataset = st.container()
user_interaction = st.container()
model = st.container()
junk = st.container()



#How to Add CSS
st.markdown(
    """
    <style>
    .main {
    background-color: #F5F5F5;
    }
    </style>
    """,
    unsafe_allow_html=True
)
@st.cache
def get_data(filename):
  data = pd.read_csv(filename)
  return data

with title:
  st.title("Fashion Designer")
  
with dataset:
  st.header("Dataset")
  images = get_data("images.csv")
  st.write(images)
  st.bar_chart(images["label"].value_counts())
  
with user_interaction:
  clothes_options = ["shirts","dresses","hats"]
  st.header("Select a clothing item from below:")
  clothes_selected = st.selectbox("Which clothing would you select?",
                                  options= clothes_options)
  st.write("Selectbox returns:",clothes_selected,
          "of type",type(clothes_selected))
  if clothes_selected == "shirts":
    st.write("You have selected a shirt")
  else:
    st.write("You have not selected a shirt")
    
  st.subheader("*Important*")
  st.write("Please note the following before uploading your item")
  st.markdown("* Rule 1")
  st.markdown("* Rule 2")
  item = st.file_uploader("Please upload a clothing item")
  st.write(item)

with model:
  st.write("This is where the model will be")
  
  
with junk:
  st.header("Ignore everything below")
  st.markdown("* First item in the list")
  st.markdown("* Second item in the list")
  st.write("Selectbox from a NumPy array")
  array = np.array([[1,2,3],[4,5,6],[7,8,9]])
  col1, mid, col2 = st.columns([1,3,3])
  with col1:
    st.write("My Array:",array)
  with mid:
    st.write("something")
  with col2:
    st.write("something else")  
  st.file_uploader("Please upload a file")

# """Write"""
# st.write("You have chosen:",clothes_options,"")
