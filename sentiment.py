from google.cloud import language_v1
from textblob import TextBlob
import json

def analyse_sentiment_textblob(text_content):
    return TextBlob(text_content).sentiment.polarity

def analyse_sentiment_google(text_content):
    """
    Perform sentiment analysis on text.

    Args:
        text_content (str): The text content to analyse.
    """

    client = language_v1.LanguageServiceClient()

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT
