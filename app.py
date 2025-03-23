import streamlit as st
import requests

st.title("AI API Generator")

# ---------------------------
# Upload Section
# ---------------------------
st.header("Upload Your AI Model")
uploaded_file = st.file_uploader("Choose a file", type=["bin", "pt", "h5", "pkl"])
if uploaded_file:
    st.success("Model uploaded successfully!")

# ---------------------------
# Generate API Link Section
# ---------------------------
st.header("Generate API Link")
api_link = "https://sentiment-api-kejl.onrender.com/predict-text"
if st.button("Generate API"):
    st.markdown(f"Your API link: [{api_link}]({api_link})")

# ---------------------------
# Prediction Section (Polished)
# ---------------------------
st.header("Test Your AI Model")
user_input = st.text_input("Enter a sentence to analyze:")

if st.button("Predict Sentiment"):
    if user_input:
        url = "https://sentiment-api-kejl.onrender.com/predict-text"
        payload = {"text": user_input}
        
        # 🌀 Show loading spinner while waiting for API
        with st.spinner("Getting prediction..."):
            response = requests.post(url, json=payload)
        
        # ✅ If successful response
        if response.status_code == 200:
            result = response.json()
            sentiment = result["sentiment"]
            confidence = round(result["confidence"] * 100, 2)
            
            # 🎯 Styled output
            st.markdown(f"### Sentiment: **{sentiment.upper()}** 🎯")
            st.markdown(f"Confidence: **{confidence}%**")
        
        # ❌ If something goes wrong
        else:
            st.error(f"API Error: {response.status_code} – {response.text}")
    else:
        st.warning("Please enter some text above.")

