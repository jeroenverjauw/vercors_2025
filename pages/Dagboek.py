import streamlit as st
from pathlib import Path
import subprocess
from subprocess import run, PIPE


st.title("Dagboek")


for i in range(1,18):
	st.image(f"data/pictures/extra/boekje_vercors25_page-{i}.jpg")