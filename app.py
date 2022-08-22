import streamlit as st
import chat_organizing

st.sidebar.title("Whatsapp Chat Analysis")

uploaded_file = st.sidebar.file_uploader("Choose file for analysis")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    chat = bytes_data.decode("utf-8")
    df = chat_organizing.preprocess(chat)

    st.dataframe(df)


