import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000/predict"

st.title("🎬 Sentiment Analysis")

review = st.text_area(
    "Enter your movie review",
    height=150,
    placeholder="Enter your review here..."
)

if st.button("Analyze Sentiment"):
    if not review.strip():
        st.warning("Please enter a review")
    else:
        response = requests.post(API_URL, json={"review": review})

        if response.status_code == 200:
            data = response.json()
            sentiment = data["sentiment"]
            score = data["score"]

            if sentiment == "Positive":
                st.success(f"Positive 👍  (Confidence: {score})")
            else:
                st.error(f"Negative 👎  (Confidence: {score})")
        else:
            st.error("API Error")
