import streamlit as st
from pathlib import Path
import os
import zipfile
from io import BytesIO
from PIL import Image
import re

st.title("Siel's media")

st.subheader("Foto's")
foto_path = "data/pictures/Siel/"


files = [i for i in os.listdir(foto_path) if '.jpg' in i.lower()]

# Extract number using regex and sort
def extract_number(filename):
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else float('inf')  # put non-numbered files last

# Sort files based on extracted numbers
files = sorted(files, key=extract_number)

for file in files:
    st.image(foto_path+file)

st.subheader("Video's")
video_path = "data/videos/Siel/"

files = os.listdir(video_path) 

for file in files:
    st.video(video_path+file)