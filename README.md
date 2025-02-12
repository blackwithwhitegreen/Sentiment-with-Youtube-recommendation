# Sentiment Analysis Chatbot - README

## Overview

The **Sentiment Analysis Chatbot** is a Streamlit-based web application that analyzes the sentiment of text inputs or uploaded files and recommends relevant YouTube videos based on the analyzed content. It leverages the **TextBlob** library for sentiment analysis and the YouTube Data API to fetch video recommendations.

---

## Features

- **Sentiment Analysis**:
  - Accepts both direct text input and file uploads (CSV or TXT format).
  - Analyzes sentiment using TextBlob and classifies it as Positive, Negative, or Neutral.
  - Provides a sentiment polarity score for detailed insight.

- **YouTube Video Recommendations**:
  - Fetches YouTube videos relevant to the input text.
  - Displays video thumbnails, titles, and links for easy access.

- **User-Friendly Interface**:
  - Clean, interactive, and responsive UI built using Streamlit.
  - Real-time feedback and error handling.

---

## Prerequisites

- Python 3.7 or higher
- A valid YouTube Data API key

---

## Installation

1. Clone the repository or copy the script to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required dependencies:
   ```bash
   pip install streamlit textblob requests pandas
   ```

3. Replace the placeholder API key (`YOUTUBE_API_KEY`) in the script with your own YouTube Data API key.

---

## Usage

1. Run the application:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and navigate to the URL displayed in the terminal (typically `http://localhost:8501`).

3. Choose an input method:
   - **Text Input**: Enter your text in the input box.
   - **File Upload**: Upload a CSV or TXT file containing text data.

4. Click the **Analyze** button to:
   - View the sentiment analysis results.
   - See the recommended YouTube videos.

---

## File Format Requirements

- **CSV File**: The first column should contain the text data to be analyzed.
- **TXT File**: Each line should contain one text entry.

---

## Project Structure

- `app.py`: The main application script.
- `requirements.txt`: A list of dependencies (optional, if packaging).

---

## Example Outputs

### Sentiment Analysis:
- **Input**: "I love programming!"
- **Sentiment**: Positive Vibes 🫰
- **Polarity Score**: 0.50

### YouTube Video Recommendations:
- Displays a grid of video thumbnails with clickable links.

---

## Customization

1. **Change the number of videos fetched**:
   - Modify the `maxResults` parameter in the `fetch_youtube_videos` function.

2. **Update the UI theme**:
   - Customize Streamlit's appearance using CSS and Streamlit configurations.

---

## Known Issues and Limitations

1. **Rate Limiting**: Ensure your API key has sufficient quota to fetch videos.
2. **Sentiment Analysis Scope**: TextBlob may not perform well on highly complex or domain-specific texts.

---

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- [Streamlit](https://streamlit.io) for the web app framework.
- [TextBlob](https://textblob.readthedocs.io) for sentiment analysis.
- [YouTube Data API](https://developers.google.com/youtube) for video recommendations.

---

Enjoy analyzing sentiment and discovering new videos! 🚀
