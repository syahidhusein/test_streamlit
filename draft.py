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

col1,col2,col3,col4 = st.columns(4)

if "photo" not in st.session_state:
    st.session_state["photo"]="not done"

def change_photo_state():
    st.session_state["photo"]="done"
    
with title:
  with col2:
    st.header("Outfit")
  with col3:
    st.header("Recommender")
  
with dataset:
  with col2:
    st.write("something")
    
with user_interaction:
  with col2:
    st.write("something else")

with model:
  with col2:
    st.write("something other than else")
