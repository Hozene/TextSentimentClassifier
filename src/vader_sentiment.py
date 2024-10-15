import os
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

class DataLoader:
    def __init__(self, base_path):
        self.base_path = base_path

    def load_data(self):
        reviews = []  # store the text of reviews
        labels = []  # store corresponding sentiment labels ('pos' or 'neg')

        # loading positive reviews
        pos_path = os.path.join(self.base_path, 'pos')
        for file in os.listdir(pos_path):
            with open(os.path.join(pos_path, file), 'r', encoding='utf-8') as f:
                reviews.append(f.read())
                labels.append('pos')

        # loading negative reviews
        neg_path = os.path.join(self.base_path, 'neg')
        for file in os.listdir(neg_path):
            with open(os.path.join(neg_path, file), 'r', encoding='utf-8') as f:
                reviews.append(f.read())
                labels.append('neg')

        return reviews, labels

class SentimentAnalyzer:
    def __init__(self):
        nltk.download('vader_lexicon')
        self.sia = SentimentIntensityAnalyzer()

    def analyze(self, text):
        return self.sia.polarity_scores(text)

class Evaluator:
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def evaluate(self, reviews):
        pos_count = 0
        neg_count = 0
        neutral_count = 0
        total = len(reviews)

        print(f"Evaluating on {total} reviews...")

        for idx, review in enumerate(reviews, start=1):
            sentiment = self.analyzer.analyze(review)
            compound_score = sentiment['compound']

            # using VADER's compound score to classify the review
            if compound_score >= 0.05:
                pos_count += 1
            elif compound_score <= -0.05:
                neg_count += 1
            else:
                neutral_count += 1

            # displaying progress every 1000 reviews
            if idx % 1000 == 0:
                print(f"Progress: {idx}/{total} reviews evaluated")

        print("\n--- Overall Sentiment Results ---")
        print(f"Positive Reviews: {pos_count}")
        print(f"Negative Reviews: {neg_count}")
        print(f"Neutral Reviews: {neutral_count}")

if __name__ == "__main__":
    print("Loading test data...")
    base_path = '../aclImdb/test'
    data_loader = DataLoader(base_path)
    reviews, labels = data_loader.load_data()
    analyzer = SentimentAnalyzer()
    evaluator = Evaluator(analyzer)
    evaluator.evaluate(reviews)
