
2. Natural Language Processing (NLP) for Bias Detection

Bias detection relies on NLP techniques to analyze sentiment, opinionated language, and loaded words in news articles. We use spaCy, TextBlob, or 
transformers for text analysis.

import spacy

from textblob import TextBlob

nlp = spacy.load("en_core_web_sm")

def detect_bias(text):

    doc = nlp(text)

    sentiment = TextBlob(text).sentiment.polarity

    biased_words = [token.text for token in doc if token.pos_ in ["ADJ", "ADV"]]
    
    return {"sentiment_score": sentiment, "biased_words": biased_words}

article = "The corrupt politician made reckless decisions."

print(detect_bias(article))

This script detects opinionated adjectives and assigns a sentiment score.