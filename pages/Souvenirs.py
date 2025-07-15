import streamlit as st
from pathlib import Path
from streamlit_pdf_viewer import pdf_viewer

from subprocess import run, PIPE


st.title("Des Petites Souvenirs")


pdf_viewer("data/pictures/extra/postkaart_voorkant.pdf") 
pdf_viewer("data/pictures/extra/postkaart_achterkant.pdf") 
st.image("data/pictures/jeroen/IMG_4129.jpg")  