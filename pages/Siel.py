import streamlit as st
from pathlib import Path
import os
from PIL import Image
import re
import zipfile
from io import BytesIO

st.title("Siel's media")

# Paths
image_folder = "data/pictures/Siel/"
video_folder = "data/videos/Siel/"

# Extract numeric sort key
def extract_number(filename):
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else float('inf')

# Get and sort files
image_files = sorted([f for f in os.listdir(image_folder) if f.lower().endswith(('jpg', 'jpeg', 'png'))], key=extract_number)
video_files = sorted([f for f in os.listdir(video_folder) if f.lower().endswith(('mp4', 'mov', 'avi'))], key=extract_number)

# Create tabs
gallery_type = st.selectbox("Select gallery type:", ["🖼️ Image Gallery", "🎬 Video Gallery"])

if gallery_type == "🖼️ Image Gallery":
    st.header("Image Gallery")

    if st.button("Create ZIP of Figures"):
    # Create in-memory ZIP file
        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zip_file:
            for fig_file in image_files:
                file_path = os.path.join(image_folder, fig_file)
                zip_file.write(file_path, arcname=fig_file)  # arcname avoids folder nesting

        zip_buffer.seek(0)

        # Provide download button
        st.download_button(
            label="Download ZIP",
            data=zip_buffer,
            file_name="figures.zip",
            mime="application/zip"
        )

    cols_per_row = st.slider("Photos per row", 1, 5, 3)

    cols = st.columns(cols_per_row)
    for idx, img_file in enumerate(image_files):
        image_path = os.path.join(image_folder, img_file)
        img = Image.open(image_path)

        with cols[idx % cols_per_row]:
            st.image(img, use_container_width=True)

# -------------------------
# Tab 2: Video Gallery
# -------------------------
elif gallery_type == "🎬 Video Gallery":
    st.header("Video Gallery")

    if st.button("Create ZIP of Figures"):
    # Create in-memory ZIP file
        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zip_file:
            for video_file in video_files:
                file_path = os.path.join(video_folder, video_file)
                zip_file.write(file_path, arcname=video_file)  # arcname avoids folder nesting

        zip_buffer.seek(0)

        # Provide download button
        st.download_button(
            label="Download ZIP",
            data=zip_buffer,
            file_name="videos.zip",
            mime="application/zip"
        )

    for video_file in video_files:
        video_path = os.path.join(video_folder, video_file)
        st.video(video_path)
