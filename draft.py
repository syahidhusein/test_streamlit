import streamlit as st
import numpy as np
import pandas as pd
import time

title = st.container()
dataset = st.container()
user_interaction = st.container()
model = st.container()
junk = st.container()

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

with col2:
  with dataset:
    st.write("something")
    
with col2:
  with user_interaction:
    st.write("something else")

with col2:
  with model:
    st.write("something other than else")
