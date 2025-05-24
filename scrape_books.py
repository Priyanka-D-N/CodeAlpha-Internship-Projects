import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate

# Step 1: Send request to the website
url = 'http://books.toscrape.com/'
response = requests.get(url)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract book data
books = soup.find_all('article', class_='product_pod')
data = []

for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    rating = book.p['class'][1]  # star-rating
    data.append({'Title': title, 'Price': price, 'Rating': rating})

# Step 4: Convert to DataFrame and display as table
df = pd.DataFrame(data)

# Display as neat table in terminal
print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

# Save to CSV
df.to_csv('books_data.csv', index=False)
print("\n✅ Scraping Complete! Data saved to books_data.csv")
