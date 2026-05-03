"""
Mood Detection Utility Module
This module provides AI-based mood detection using TextBlob sentiment analysis.
"""

from textblob import TextBlob


def detect_mood(text):
    """
    Detects mood from user input text using sentiment analysis.
    
    Args:
        text (str): User input text to analyze
        
    Returns:
        str: Detected mood - "Happy", "Sad", or "Stressed"
        
    Logic:
        - polarity > 0.3 → "Happy" (positive sentiment)
        - polarity < -0.3 → "Sad" (negative sentiment)  
        - otherwise → "Stressed" (neutral/mixed sentiment)
        
    Example:
        >>> detect_mood("I am so happy and excited!")
        'Happy'
        >>> detect_mood("I feel very sad and lonely")
        'Sad'
        >>> detect_mood("I don't know how to feel")
        'Stressed'
    """
    
    # ✅ Return "Neutral" if text is empty
    if not text or not text.strip():
        return "Stressed"
    
    # ✅ Create TextBlob object and get polarity
    # Polarity ranges from -1 (negative) to 1 (positive)
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    # ✅ Classify mood based on polarity thresholds
    if polarity > 0.3:
        return "Happy"
    elif polarity < -0.3:
        return "Sad"
    else:
        return "Stressed"
