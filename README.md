# Sentiment Analysis Project

## Overview
This project aims to perform sentiment analysis on movie reviews using different methodologies: VADER (Valence Aware Dictionary and sEntiment Reasoner) and neural networks. The dataset used for this analysis is the **[Large Movie Review Dataset](https://ai.stanford.edu/~amaas/data/sentiment/)**, which contains labeled reviews for training and testing the models.

## Approaches
We will implement the following approaches for sentiment analysis:

### 1. VADER Sentiment Analysis
- **Description**: VADER is a pre-trained sentiment analysis tool specifically designed for determining whether a piece of writing is positive, negative, or neutral. It uses a lexicon of sentiment-related words and their associated sentiment scores.
- **File**: `src/vader_sentiment.py`
- **Functionality**: This script loads the test dataset and evaluates the sentiment of each review using VADER, categorizing them as positive, negative, or neutral based on the compound score provided by VADER.

### 2. Neural Network Approaches (In progress)
...

## Dataset
For the description of the dataset go [**Here**](https://ai.stanford.edu/~amaas/data/sentiment/) and see its `README` file after downloading  

### Works Cited 
- Maas, Andrew L., et al. ‘Learning Word Vectors for Sentiment Analysis’. Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies, Association for Computational Linguistics, 2011, pp. 142–150, http://www.aclweb.org/anthology/P11-1015.