
from PIL import Image
import streamlit as st
import pandas as pd
import os
from pathlib import Path

st.title("Sydnaes Taylor Swift Application")
folder_dir = os.path.join(Path(__file__).parents[0])
counties = pd.read_csv(f'{folder_dir}\\data\\ts.png', low_memory=False)


image_path = 'C:/Users/jjs61/OneDrive/Desktop/News/src/data/ts.png'
image = Image.open(image_path)
st.image(image, caption="Sydnea's lover", use_column_width=True)




st.write('''
        This app connects to the newapi.org API and searches for previous day Taylor Swift news articles. 
    ''')

