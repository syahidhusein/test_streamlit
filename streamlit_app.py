"""This is a test for streamlit"""
import streamlit as st
import numpy as np
"""Title"""
st.title("Fashion Designer")
"""Header"""
clothes_options = ["shirts","dresses","hats"]
st.header("Select a clothing item from below:")
clothes_selected = st.selectbox("Which clothing would you select?",
                                options= clothes_options)
""""file uploader"""
st.file_uploader("Please upload a file")
# """Write"""
# st.write("You have chosen:",clothes_options,"")
