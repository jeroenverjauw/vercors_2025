import streamlit as st
from pathlib import Path
import os
import zipfile
from io import BytesIO
from PIL import Image
import re

st.title("Siel's media")

image_folder = "data/pictures/Siel/"
video_folder = "data/videos/Siel/"

def extract_number(filename):
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else float('inf')  # put non-numbered files last

# Sort files based on extracted numbers
image_files = sorted([f for f in os.listdir(image_folder) if f.lower().endswith(('jpg', 'jpeg', 'png'))], key=extract_number)

# File filters
video_files = sorted([f for f in os.listdir(video_folder) if f.lower().endswith(('mp4', 'mov', 'avi'))],key = extract_number)

# Setup session state
if "selected_image" not in st.session_state:
    st.session_state.selected_image = None 

if "selected_video" not in st.session_state:
    st.session_state.selected_video = None

# Tabs
tab1, tab2 = st.tabs(["🖼️ Image Gallery", "🎬 Video Gallery"])

# st.subheader("Foto's")
# foto_path = "data/pictures/Siel/"


# files = [i for i in os.listdir(foto_path) if '.jpg' in i.lower()]

with tab1:
    st.header("Image Gallery")

    # Set up number of columns
    cols_per_row = st.slider("Photo's per row", 1, 5, 1, step=1)

    # Display images in a grid 
    cols = st.columns(cols_per_row)
    for idx, img_file in enumerate(image_files):
        st.write(img_file)
        image_path = os.path.join(image_folder, img_file)
        img = Image.open(image_path)

        # Use button with image thumbnail
        with cols[idx % cols_per_row]:
            st.image(img, use_container_width=True)

    st.markdown("---")


with tab2:
    st.header("Video Gallery")   

    for file in video_files:
        st.video(video_folder+file)