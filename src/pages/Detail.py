import streamlit as st
from sqlalchemy import create_engine
import pandas as pd

# web application header
st.title('Taylor Swift Detailed Content')



# Make Connection
db_url = 'postgresql://postgres:sydney187@localhost/swift'
engine = create_engine(db_url)


query = 'SELECT * FROM tswift;'
df = pd.read_sql(query, engine)

selected_columns = ['content','source', 'title', 'description', 'nfl_presence', 'sex_or_ex_presence', 'url']

# Filter the DataFrame to keep only the selected columns
df = df[selected_columns]
df = df.dropna()


st.dataframe(df)


# Create a chart that groups sources and counts articles
st.subheader('Articles by Author')
source_counts = df['source'].value_counts()
st.bar_chart(source_counts)
