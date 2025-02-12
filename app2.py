import streamlit as st
from textblob import TextBlob
import requests
import pandas as pd

# Streamlit UI configuration
st.set_page_config(
    page_title="Sentiment Analysis Chatbot",
    page_icon="💬",
    layout="centered",
)

# API Key (replace with your own)
YOUTUBE_API_KEY = "AIzaSyBdfKFYrq77rz5RitMUuG-54Qo_XUfoLQw"

# Function to fetch YouTube videos
def fetch_youtube_videos(query):
    base_url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "key": YOUTUBE_API_KEY,
        "type": "video",
        "maxResults": 6,
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return [
            {
                "title": item["snippet"]["title"],
                "link": f"https://www.youtube.com/watch?v={item['id']['videoId']}",
                "thumbnail": item["snippet"]["thumbnails"]["medium"]["url"],
            }
            for item in data.get("items", [])
        ]
    return []

# Title and description
st.title("💬 Try me!! I know every thing.")
st.markdown(
    "Select the file type text or CSV file,"
)

# Input options: Text box and file upload
input_type = st.radio("Input Type:", ["Text", "Upload File"], horizontal=True)

if input_type == "Text":
    user_input = st.text_input("You:", placeholder="Type your message here...")
elif input_type == "Upload File":
    uploaded_file = st.file_uploader("Upload a CSV or Text file:", type=["csv", "txt"])

# Sentiment Analysis and Recommendations
if st.button("Analyze"):
    if input_type == "Text" and user_input.strip():
        inputs = [user_input]
    elif input_type == "Upload File" and uploaded_file:
        if uploaded_file.type == "text/csv":
            data = pd.read_csv(uploaded_file)
            inputs = data.iloc[:, 0].dropna().tolist()
        elif uploaded_file.type == "text/plain":
            inputs = uploaded_file.getvalue().decode("utf-8").splitlines()
        else:
            st.error("Unsupported file format!")
            inputs = []
    else:
        st.error("Please provide a valid input!")
        inputs = []

    if inputs:
        for input_text in inputs:
            st.markdown(f"#### Input: {input_text}")

            # Analyze sentiment
            analysis = TextBlob(input_text)
            sentiment_score = analysis.sentiment.polarity
            sentiment = (
                "Positive Vibes 🫰"
                if sentiment_score > 0
                else "Negative, that hurt💔💔, lier"
                if sentiment_score < 0
                else "Neutral - chle ja yha sye.."
            )

            # Display sentiment results
            st.markdown(f"**Sentiment:** {sentiment}")
            st.markdown(f"**Polarity Score:** {sentiment_score:.2f}")

            # Fetch and display YouTube videos
            st.markdown("### 🎥 The best output according to me... let's see")
            youtube_videos = fetch_youtube_videos(input_text)
            if youtube_videos:
                cols = st.columns(3)  # 3 videos per row
                for idx, video in enumerate(youtube_videos):
                    with cols[idx % 3]:  # Distribute cards across columns
                        st.markdown(
                            f"""
                            <div style="
                                border: 1px solid #ddd; 
                                border-radius: 10px; 
                                padding: 10px; 
                                margin-bottom: 20px; 
                                text-align: center; 
                                background-color: #f9f9f9;
                                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                            ">
                                <img src="{video['thumbnail']}" alt="{video['title']}" style="width: 100%; height: auto; border-radius: 10px;">
                                <h4 style="margin-top: 10px; font-size: 16px; color: #333;">
                                    <a href="{video['link']}" target="_blank" style="text-decoration: none; color: #0073e6;">{video['title']}</a>
                                </h4>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )
            else:
                st.info("No YouTube videos found for this query.")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using [Streamlit](https://streamlit.io).")


