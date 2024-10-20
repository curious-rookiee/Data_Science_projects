import matplotlib.pyplot as plt
from libraries import * 
from operations import summarize_text, analyze_sentiment

def main():
    # Load reviews from input CSV file
    input_file_path = 'sentiment_input.csv'  # Update with your actual file path
    with open(input_file_path, 'r') as file:
        review_lines = file.readlines()

    # Analyze sentiment of reviews
    positive_reviews, neutral_reviews, negative_reviews = analyze_sentiment(review_lines)

    # Plotting the number of reviews in each sentiment class using a pie chart
    sentiment_labels = ['Positive', 'Neutral', 'Negative']
    review_counts = [len(positive_reviews), len(neutral_reviews), len(negative_reviews)]

    plt.figure(figsize=(8, 6))
    plt.pie(review_counts, labels=sentiment_labels, autopct='%1.1f%%', startangle=140, colors=['green', 'gray', 'red'])
    plt.title('Distribution of Reviews by Sentiment Class')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

    # Summarizing the reviews for each sentiment class
    positive_summary_text = "\n".join(positive_reviews)
    neutral_summary_text = "\n".join(neutral_reviews)
    negative_summary_text = "\n".join(negative_reviews)

    positive_summary = summarize_text(positive_summary_text)
    neutral_summary = summarize_text(neutral_summary_text)
    negative_summary = summarize_text(negative_summary_text)

    # Print the summaries
    print("Positive Summary:", positive_summary)
    print("Neutral Summary:", neutral_summary)
    print("Negative Summary:", negative_summary)

    # Save summaries to separate files
    with open('positive_summary.txt', 'w') as positive_file:
        positive_file.write(positive_summary)

    with open('neutral_summary.txt', 'w') as neutral_file:
        neutral_file.write(neutral_summary)

    with open('negative_summary.txt', 'w') as negative_file:
        negative_file.write(negative_summary)

    print("Summaries have been saved to positive_summary.txt, neutral_summary.txt, and negative_summary.txt.")

if __name__ == '__main__':
    main()
