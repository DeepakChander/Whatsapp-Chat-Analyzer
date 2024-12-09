import re
import pandas as pd
def preprocess(data):
    pattern = '\d{2}/\d{2}/\d{2}, \d{1,2}:\d{2}(?:\s?(?:AM|PM|am|pm))? -\s'

    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    df = pd.DataFrame({'user_message': messages, 'message_dates': dates})
    df['message_dates'] = df['message_dates'].str.replace(r'([APap][Mm])', r' \1', regex=True)

    # Now convert the dates with the corrected format
    df['message_dates'] = pd.to_datetime(df['message_dates'], format='%d/%m/%y, %I:%M %p - ')

    # Rename the column after converting it
    df.rename(columns={'message_dates': 'date'}, inplace=True)

    users = []
    messages = []
    for message in df['user_message']:
        # Try to split the message into user and message content
        entry = re.split(r'([\w\W]+?):\s', message, maxsplit=1)

        # If the entry has a valid user and message
        if len(entry) > 2:
            users.append(entry[1])  # User name
            messages.append(entry[2])  # Message content
        else:
            users.append('group_notification')  # Handle system messages or group notifications
            messages.append(entry[0])  # The whole message is the notification

    # Add the parsed users and messages into the DataFrame
    df['user'] = users
    df['message'] = messages

    # Drop the original 'user_message' column
    df.drop(columns=['user_message'], inplace=True)

    df['year'] = df['date'].dt.year
    df['only_date'] = df['date'].dt.date
    df['day_name'] = df['date'].dt.day_name()
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['minute'] = df['date'].dt.minute

    return df