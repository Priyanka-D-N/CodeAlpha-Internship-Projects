import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Load reviews
df = pd.read_csv("reviews.csv")

# Analyze sentiment
def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

df['Sentiment'] = df['Review'].apply(get_sentiment)

# Display results
print("🔹 Sentiment Summary:")
print(df['Sentiment'].value_counts())
print("\n🔹 Sample Analysis:")
print(df.head())

# Plot Sentiment Count
plt.figure(figsize=(6, 4))
df['Sentiment'].value_counts().plot(kind='bar', color=['green', 'red', 'gray'])
plt.title('Sentiment Analysis Result')
plt.xlabel('Sentiment')
plt.ylabel('Number of Reviews')
plt.tight_layout()
plt.show()
