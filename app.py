import streamlit as st
import chat_organizing, help
import matplotlib.pyplot as plt
import seaborn as sns

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
        num_messages, words, num_media_messages, num_links = help.fetch_stats(selected_user, df)
        
        col1, col2, col3, col4 = st.beta_columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Media Shared")
            st.title(num_media_messages)
        with col4:
            st.header("Links Shared")
            st.title(num_links)

        if selected_user == 'Overall':
            st.title('Most Busy Users')
            x, new_df = help.most_busy_user(df)
            fig, ax = plt.subplots()

            col1, col2 = st.beta_columns(2)

            with col1:
                ax.bar(x.index, x.values)
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

            with col2:
                st.dataframe(new_df)

        st.title("Wordcloud")
        df_wc = help.create_wordcloud(selected_user, df)
        fig, ax = plt.subplot()
        ax.imshow(df_wc)
        st.pyplot(fig)