from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Initialize FastAPI app
app = FastAPI()

# Load pre-trained sentiment analysis model from Hugging Face
classifier = pipeline("sentiment-analysis")

# Define the input format (expects JSON: {"text": "some text"})
class TextInput(BaseModel):
    text: str
    
# Create a simple endpoint for AI predictions
@app.post("/predict-text")
def predict_sentiment(data: TextInput):
    result = classifier(data.text)
    return {"sentiment": result[0]['label'], "confidence": result[0]['score']} 
    
'''def predict_sentiment(data: TextInput):
    # Placeholder logic (replace with AI model later)
    if "good" in data.text.lower():
        return {"sentiment": "Positive"}
    else:
        return {"sentiment": "Negative"} '''