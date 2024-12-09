import streamlit as st
import os
import preprocessor, helper
import matplotlib.pyplot as plt

# Set dynamic port for deployment
port = int(os.getenv("PORT", 8501))
os.system(f"streamlit run app.py --server.port {port} --server.address 0.0.0.0")

# Custom CSS for page styling
st.markdown("""
    <style>
        /* General Page Layout */
        .main-title {
            color: #4CAF50;
            font-size: 32px;
            text-align: center;
            font-weight: bold;
        }

        /* Sidebar styling */
        .sidebar .css-1d391kg {
            border: 2px solid #4CAF50;
            padding: 10px;
        }

        /* Section Heading Styling */
        h1, h2, h3 {
            color: #333;
            font-family: 'Arial', sans-serif;
            font-weight: bold;
        }

        /* Add a container box for individual charts */
        .container {
            padding: 15px;
            background-color: #f8f9fa;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 15px;
        }

        /* Add animations to transitions (for responsiveness) */
        .stButton > button:hover {
            background-color: #45a049;
            color: white;
            transform: scale(1.05);
            transition: all 0.2s ease-in-out;
        }
    </style>
    """, unsafe_allow_html=True)

# Page Title & Branding
st.markdown("<div class='main-title'>WhatsApp Chat Analysis Dashboard 🚀</div>", unsafe_allow_html=True)

# Streamlit Sidebar Title
st.sidebar.title("🔎 WhatsApp Chat Analyzer")

# File Uploader
uploaded_file = st.sidebar.file_uploader("📂 Upload WhatsApp Chat File")

if uploaded_file is not None:
    # Read uploaded file and preprocess data
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    # Fetch unique users, excluding group notifications
    user_list = df['user'].unique().tolist()
    if "group_notification" in user_list:
        user_list.remove("group_notification")
    user_list.sort()
    user_list.insert(0, "Overall")  # Add "Overall" as the first option for general analysis

    # User selection dropdown
    selected_user = st.sidebar.selectbox("👤 Analyze messages for:", user_list)

    # Button to trigger analysis
    if st.sidebar.button("🔍 Analyze Data"):
        # Get statistics data
        num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)

        # Top Statistics Section
        st.markdown("<div class='container'>", unsafe_allow_html=True)
        st.title("📊 Top Statistics")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.subheader(num_messages)

        with col2:
            st.header("Total Words")
            st.subheader(words)

        with col3:
            st.header("Media Shared")
            st.subheader(num_media_messages)

        with col4:
            st.header("Links Shared")
            st.subheader(num_links)
        st.markdown("</div>", unsafe_allow_html=True)

        # Monthly Message Timeline Section
        st.markdown("<div class='container'>", unsafe_allow_html=True)
        st.title("📅 Monthly Timeline")
        timeline_df = helper.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(timeline_df['time'], timeline_df['message'], color='green')
        plt.xticks(rotation=45)  # Fix x-axis tick rotation
        st.pyplot(fig)
        st.markdown("</div>", unsafe_allow_html=True)

        # Daily Message Timeline Section
        st.markdown("<div class='container'>", unsafe_allow_html=True)
        st.title("🗓️ Daily Timeline")
        daily_df = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_df['only_date'], daily_df['message'], color='black')
        plt.xticks(rotation=45)  # Fix x-axis tick rotation
        st.pyplot(fig)
        st.markdown("</div>", unsafe_allow_html=True)

        # Weekly Activity Map Section
        st.markdown("<div class='container'>", unsafe_allow_html=True)
        st.title("📊 Weekly Activity Map")
        col1, col2 = st.columns(2)

        with col1:
            st.header("Most Active Day")
            weekly_activity = helper.week_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(weekly_activity.index, weekly_activity.values, color='blue')
            plt.xticks(rotation=45)  # Fix x-axis tick rotation
            st.pyplot(fig)

        with col2:
            st.header("Most Active Month")
            monthly_activity = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(monthly_activity.index, monthly_activity.values, color='orange')
            plt.xticks(rotation=45)  # Fix x-axis tick rotation
            st.pyplot(fig)

        st.markdown("</div>", unsafe_allow_html=True)

        # WordCloud Visualization Section
        st.markdown("<div class='container'>", unsafe_allow_html=True)
        st.title("🖋️ WordCloud")
        wordcloud_image = helper.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(wordcloud_image, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig)
        st.markdown("</div>", unsafe_allow_html=True)

        # Most Common Words Section
        st.markdown("<div class='container'>", unsafe_allow_html=True)
        st.title("📊 Most Common Words")
        most_common_df = helper.most_common_words(selected_user, df)

        if not most_common_df.empty:
            fig, ax = plt.subplots()
            ax.bar(most_common_df['Word'], most_common_df['Frequency'], color='purple')
            plt.xticks(rotation=45)  # Fix x-axis tick rotation
            st.pyplot(fig)
        else:
            st.info("No common words found in this analysis.")
        st.markdown("</div>", unsafe_allow_html=True)
