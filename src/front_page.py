
from PIL import Image
import streamlit as st

st.title("Sydnaes Taylor Swift Application")

image_path = 'C:/Users/jjs61/OneDrive/Desktop/News/src/data/ts.png'
image = Image.open(image_path)
st.image(image, caption="Sydnea's lover", use_column_width=True)




st.write('''
        This app connects to the newapi.org API and searches for previous day Taylor Swift news articles. 
    ''')

