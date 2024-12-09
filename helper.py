from urlextract import URLExtract
extract = URLExtract()
from wordcloud import WordCloud
import pandas as pd
from collections import Counter

def fetch_stats(selected_user,df):

    if selected_user != 'Overall':
        df=df[df['user'] == selected_user]

    # fetch the number of messages
    num_messages = df.shape[0]

    # fetch the total number of words
    words = []
    for message in df['message']:
        words.extend(message.split())

    # fetch number of media messages
        num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

    #fetch number of linked shared
        links = []
        for message in df['message']:
            links.extend(extract.find_urls(message))

        return num_messages,len(words), num_media_messages, len(links)

def most_busy_users(df):
    x = df['user'].value_counts()
    df = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'user': 'name', 'count': 'percent'})

    return x,df


def create_wordcloud(selected_user, df):
    # Read stop words from the file
    with open('stop_hinglish.txt', 'r') as f:
        stop_words = f.read()

    # Filter messages based on selected user
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # Remove group notifications and media messages for all cases
    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    # Function to remove stop words
    def remove_stop_words(message):
        y = []
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)

    # Apply stop words removal and create word cloud
    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    temp['message'] = temp['message'].apply(remove_stop_words)
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))

    return df_wc

def most_common_words(selected_user, df):
    # Open stop words file
    with open('stop_hinglish.txt', 'r') as f:
        stop_words = f.read().splitlines()  # Convert stop words to a list

    # Filter the DataFrame for the selected user
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # Filter out group notifications and media omitted messages
    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    words = []

    # Extract words from the messages, excluding stop words
    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    # Check if any words exist
    if words:
        # Create a DataFrame with most common words
        most_common_df = pd.DataFrame(Counter(words).most_common(20), columns=['Word', 'Frequency'])
        return most_common_df
    else:
        return pd.DataFrame(columns=['Word', 'Frequency'])  # Return an empty DataFrame if no words

def monthly_timeline(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()
    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))

    timeline['time'] = time

    return timeline

def daily_timeline(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    daily_timeline = df.groupby('only_date').count()['message'].reset_index()

    return  daily_timeline

def week_activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()

def month_activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()