
from PIL import Image
import streamlit as st
import pandas as pd
import os
from pathlib import Path

st.title("Sydnaes Taylor Swift Application")
folder_dir = os.path.join(Path(__file__).parents[0])



image_path1 = f'{folder_dir}\\data\\ts.png'
image1 = Image.open(image_path1)
st.image(image1, caption="Sydnea's lover", use_column_width=True)




st.write('''
        This app connects to the newapi.org API and searches for previous day Taylor Swift news articles. 
    ''')

