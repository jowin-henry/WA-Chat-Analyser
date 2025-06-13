import streamlit as st
import preprocess
import stats
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates

st.sidebar.title("Whatsapp Chat Analyzer")

# File uploader in sidebar
uploaded_file = st.sidebar.file_uploader("Choose a file")

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")

    # Preprocess the data
    df = preprocess.preprocess(data)

    # Fetch unique users excluding 'Group Notification'
    user_list = df['User'].unique().tolist()
    if 'Group Notification' in user_list:
        user_list.remove('Group Notification')
    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("Show analysis with respect to", user_list)

    st.title("Whats App Chat Analysis for " + selected_user)

    if st.sidebar.button("Show Analysis"):

        # Fetch stats for selected user
        num_messages, num_words, media_omitted, links = stats.fetchstats(selected_user, df)

        # Display stats in 4 columns
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total No.of Words")
            st.title(num_words)
        with col3:
            st.header("Media Shared")
            st.title(media_omitted)
        with col4:
            st.header("Total Links Shared")
            st.title(links)

        # Most busy users (only for Overall)
        if selected_user == 'Overall':
            st.title('Most Busy Users')
            busycount, newdf = stats.fetchbusyuser(df)
            fig, ax = plt.subplots()
            col1, col2 = st.columns(2)
            with col1:
                ax.bar(busycount.index, busycount.values, color='red')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                st.dataframe(newdf)

        # Word Cloud
        st.title('Word Cloud')
        df_img = stats.createwordcloud(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(df_img)
        ax.axis('off')  # Hide axes for better visualization
        st.pyplot(fig)

        # Most common words
        most_common_df = stats.getcommonwords(selected_user, df)
        fig, ax = plt.subplots()
        ax.barh(most_common_df[0], most_common_df[1])
        plt.xticks(rotation='vertical')
        st.title('Most common words')
        st.pyplot(fig)

        # Emoji Analysis
        emoji_df = stats.getemojistats(selected_user, df)
        emoji_df.columns = ['Emoji', 'Count']
        st.title("Emoji Analysis")
        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(emoji_df)
        with col2:
            emojicount = list(emoji_df['Count'])
            perlist = [(i / sum(emojicount)) * 100 for i in emojicount]
            emoji_df['Percentage use'] = np.array(perlist)
            st.dataframe(emoji_df)

        # # Monthly timeline with improved x-axis formatting
        # st.title("Monthly Timeline")
        # time = stats.monthtimeline(selected_user, df)
        # time['Time'] = pd.to_datetime(time['Time'])

        # fig, ax = plt.subplots()
        # ax.plot(time['Time'], time['Message'], color='green')

        # # Major ticks at start of each year
        # ax.xaxis.set_major_locator(mdates.YearLocator())
        # ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

        # # Minor ticks at Jan and Jul each year
        # ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonth=[1, 7]))
        # ax.xaxis.set_minor_formatter(mdates.DateFormatter('%b'))

        # # Rotate and style major tick labels (years)
        # plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right', fontsize=10)

        # # Rotate and style minor tick labels (months)
        # plt.setp(ax.xaxis.get_minorticklabels(), rotation=90, fontsize=8)

        # # Optional: show grid lines on minor ticks for clarity
        # ax.grid(which='minor', linestyle='--', alpha=0.5)

        # plt.tight_layout()
        # st.pyplot(fig)

        # Activity maps
        st.title("Activity Maps")
        col1, col2 = st.columns(2)
        with col1:
            st.header("Most Busy Day")
            busy_day = stats.weekactivitymap(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values, color='purple')
            plt.xticks(rotation='vertical')
            plt.tight_layout()
            st.pyplot(fig)
        with col2:
            st.header("Most Busy Month")
            busy_month = stats.monthactivitymap(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color='orange')
            plt.xticks(rotation='vertical')
            plt.tight_layout()
            st.pyplot(fig)
