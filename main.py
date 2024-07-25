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