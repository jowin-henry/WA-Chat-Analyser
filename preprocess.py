# 

import re
import pandas as pd

def gettimeanddate(text):
    # Example input: '[19/01/24, 1:33:12 PM] '
    # Strip square brackets and trailing space
    # Replace narrow no-break space \u202f with normal space for consistent parsing
    text = text.strip('[] ').replace('\u202f', ' ')
    return text  # e.g. '19/01/24, 1:33:12 PM'

def getstring(text):
    # Return only the first line in case of multiline messages
    return text.split('\n')[0]

def preprocess(data):
    # Regex pattern for timestamps like: [19/01/24, 1:33:12 PM] 
    pattern = r'\[\d{2}/\d{2}/\d{2}, \d{1,2}:\d{2}:\d{2}\u202f[AP]M\] '

    # Split messages by timestamps; first element is empty if data starts with timestamp, so discard
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    df = pd.DataFrame({'user_messages': messages, 'message_date': dates})

    # Clean timestamp strings
    df['message_date'] = df['message_date'].apply(gettimeanddate)

    # Parse timestamps to datetime objects (2-digit year format, 12-hour clock with AM/PM)
    df['Date'] = pd.to_datetime(df['message_date'], format='%y/%m/%d, %I:%M:%S %p')

    users = []
    messages = []

    for message in df['user_messages']:
        # Try to split user and message by first ": " occurrence
        entry = re.split(r'([\w\W]+?):\s', message)
        if len(entry) >= 3:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            # No user found — treat as group notification
            users.append('Group Notification')
            messages.append(entry[0])

    df['User'] = users
    df['Message'] = list(map(getstring, messages))

    # Drop columns no longer needed
    df = df.drop(['user_messages', 'message_date'], axis=1)

    # Extract useful date/time features for analysis
    df['Only date'] = df['Date'].dt.date
    df['Year'] = df['Date'].dt.year
    df['Month_num'] = df['Date'].dt.month
    df['Month'] = df['Date'].dt.month_name()
    df['Day'] = df['Date'].dt.day
    df['Day_name'] = df['Date'].dt.day_name()
    df['Hour'] = df['Date'].dt.hour
    df['Minute'] = df['Date'].dt.minute

    return df
