import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

column1, column2 = st.columns(2)

with column1:
    st.image("images/photo.png", width=640)

with column2:
    st.title("David Pechacek")
    content = """
        My name is David Pechacek.  I am a developer working to learn Python. But that's not really me over there.
    """
    st.write(content)

content2 = """
Below you can find some of the apps I've built in Python.
"""
st.write(content2)

column3, empty_col, column4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")

with column3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=640)
        st.write(f"[Source Code]({row['url']})")

with column4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=640)
        st.write(f"[Source Code]({row['url']})")