from google.cloud import language_v1
from textblob import TextBlob
import json

def analyse_sentiment_textblob(text_content):
    return TextBlob(text_content).sentiment.polarity
