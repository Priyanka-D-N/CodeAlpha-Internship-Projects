import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the scraped CSV file
df = pd.read_csv('books_data.csv',encoding='latin1')

# Step 2: Basic info
print("🔹 First 5 entries:")
print(df.head())

print("\n🔹 Dataset Info:")
print(df.info())

print("\n🔹 Null Values Check:")
print(df.isnull().sum())

print("\n🔹 Unique Ratings:")
print(df['Rating'].value_counts())

# Step 3: Clean up rating (convert text to number for graphs)
rating_map = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
}
df['Rating_Num'] = df['Rating'].map(rating_map)

# Step 4: Summary statistics
# Fix encoding characters and clean price column
df['Price'] = df['Price'].str.encode('utf-8').str.decode('utf-8', errors='ignore')  # remove encoding junk
df['Price'] = df['Price'].str.replace('Â', '', regex=False)
df['Price'] = df['Price'].str.replace('Ã\x82', '', regex=False)
df['Price'] = df['Price'].str.replace('£', '', regex=False)
df['Price'] = df['Price'].str.replace('[^0-9.]', '', regex=True)  # Remove any remaining unwanted characters
df['Price'] = df['Price'].astype(float)

# Display statistics
print("\n🔹 Cleaned Price Statistics:")
print(df['Price'].describe())

# 📊 1. Rating Count Bar Chart
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='Rating', order=df['Rating'].value_counts().index, palette='Set2')
plt.title('Number of Books by Rating')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()

# 💰 2. Price Distribution Histogram
plt.figure(figsize=(8,5))
sns.histplot(df['Price'], kde=True, color='skyblue', bins=10)
plt.title('Distribution of Book Prices')
plt.xlabel('Price (£)')
plt.ylabel('Frequency')
plt.show()

# 🏷️ 3. Top 10 Expensive Books (Horizontal Bar Plot)
top_10 = df.sort_values(by='Price', ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(data=top_10, x='Price', y='Title', palette='viridis')
plt.title('Top 10 Most Expensive Books')
plt.xlabel('Price (£)')
plt.ylabel('Book Title')
plt.tight_layout()
plt.savefig("rating_chart.png")
plt.show()
