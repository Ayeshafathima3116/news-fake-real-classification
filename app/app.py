#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import joblib
import string
from nltk.corpus import stopwords
import nltk

# Download stopwords if not already downloaded
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Load model and vectorizer
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Function to clean text
def clean_text(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

# Streamlit App
st.title("📰 Fake News Detector")
st.write("Paste any news article text below to check whether it's **Fake** or **Real**.")

# User input
user_input = st.text_area("Enter News Article Text", height=200)

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Clean and vectorize
        cleaned = clean_text(user_input)
        vect_text = vectorizer.transform([cleaned])
        prediction = model.predict(vect_text)

        # Show result
        if prediction[0] == 1:
            st.success("✅ This news is **REAL**.")
        else:
            st.error("🚫 This news is **FAKE**.")

