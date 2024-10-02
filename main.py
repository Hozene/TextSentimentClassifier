import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

texts = [
    "I love this product! It's amazing.",
    "I'm really disappointed with the service.",
    "The movie was okay, not great but not bad either."
]

for text in texts:
    sentiment = sia.polarity_scores(text)
    print(f"Text: {text}\nSentiment: {sentiment}")
