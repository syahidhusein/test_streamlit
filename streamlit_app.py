"""This is a test for streamlit"""
import streamlit as st
import numpy as np
import pandas as pd
"""Title"""
st.title("Fashion Designer")
"""Header"""
clothes_options = ["shirts","dresses","hats"]
st.header("Select a clothing item from below:")
clothes_selected = st.selectbox("Which clothing would you select?",
                                options= clothes_options)
"""Write"""
st.write("Selectbox returns:",clothes_selected,
        "of type",type(clothes_selected))
if clothes_selected == "shirts":
  st.write("You have selected a shirt")
else:
  st.write("You have not selected a shirt")

st.header("Selectbox from a NumPy array")
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
col1, mid, col2 = st.columns([1,0.1,3])
print(array)

"""File uploader"""
st.file_uploader("Please upload a file")

# """Write"""
# st.write("You have chosen:",clothes_options,"")
