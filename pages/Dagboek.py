import streamlit as st
from pathlib import Path
import subprocess
from subprocess import run, PIPE
from streamlit_pdf_viewer import pdf_viewer

st.title("Dagboek")

pdf_viewer("data/pictures/extra/boekje_vercors25.pdf")