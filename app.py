import streamlit as st
import chat_organizing, help

st.sidebar.title("Whatsapp Chat Analysis")

uploaded_file = st.sidebar.file_uploader("Choose file for analysis")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    chat = bytes_data.decode("utf-8")
    df = chat_organizing.preprocess(chat)

    st.dataframe(df)
    
    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("Show analysis accordingly", user_list)

    if st.sidebar.button("Show Analysis"):
        num_messages, words = help.fetch_stats(selected_user, df)
        
        col1, col2, col3, col4 = st.beta_columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)