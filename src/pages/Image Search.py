import streamlit as st
from sqlalchemy import create_engine
import pandas as pd

# Web application header
st.title('Taylor Swift Detailed Content')

# Make Connection
db_url = 'postgresql://postgres:sydney187@localhost/swift'
engine = create_engine(db_url)

# Query to retrieve articles
query = 'SELECT * FROM tswift;'
df = pd.read_sql(query, engine)
df = df.dropna()


# Create a list of article titles for selection
article_titles = df['title'].tolist()
selected_article = st.selectbox('Select an article:', article_titles)

# Display the selected article's image
if selected_article:
    selected_row = df[df['title'] == selected_article]
    selected_image_url = selected_row['urltoimage'].values[0]
    st.image(selected_image_url)

    
    # Display the selected article's text
    selected_text = selected_row['content'].values[0]
    st.write(selected_text)


