# operations.py

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

def summarize_text(text):
    stop_words_set = set(stopwords.words('english'))
    tokenized_words = word_tokenize(text.lower())

    # Filter words to remove stop words
    filtered_words = [word for word in tokenized_words if word.isalpha() and word not in stop_words_set]

    # Calculate word frequencies
    word_frequency = nltk.FreqDist(filtered_words)

    # Tokenize the text into sentences
    sentence_list = sent_tokenize(text)

    # Ensure there are sentences to score
    if not sentence_list:
        return "No sentences found to summarize."

    # Initialize a dictionary to hold sentence scores
    sentence_scores = {}
    for sentence in sentence_list:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequency:
                # Score the sentence based on the frequency of the words it contains
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_frequency[word]
                else:
                    sentence_scores[sentence] += word_frequency[word]

    # Sort the sentences by score in descending order
    if not sentence_scores:
        return "No sentences scored for summary."

    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:3]  # Select top 3 sentences

    # Create a summary from the selected top sentences
    summary_result = ' '.join(top_sentences)

    # Clean up sentence endings for better readability
    summary_result = summary_result.replace(";", ".").replace(".", ". ")  # Optional: adjust punctuation

    return summary_result.strip()

def analyze_sentiment(reviews):
    # Initialize Sentiment Intensity Analyzer
    sentiment_analyzer = SentimentIntensityAnalyzer()

    # Categorize reviews based on sentiment
    positive_reviews = []
    neutral_reviews = []
    negative_reviews = []

    for review in reviews:
        review = review.strip()
        sentiment_score = sentiment_analyzer.polarity_scores(review)
        compound_score = sentiment_score['compound']

        if compound_score >= 0.5:
            positive_reviews.append(review)
        elif compound_score <= -0.2:
            negative_reviews.append(review)
        else:
            neutral_reviews.append(review)

    return positive_reviews, neutral_reviews, negative_reviews
