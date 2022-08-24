from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji

extract = URLExtract()

def fetch_stats(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user].shape[0]

    num_messages = df.shape[0]
    words = []
    for message in df['message']:
        words.extend(message.split())

        num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

        links = []
        for message in df['message']:
            links.extend(extract.find_urls(message))
        
    return num_messages, len(words), num_media_messages, len(links)

def most_busy_user(df):
    x = df['user'].value_counts().head()

    return x
