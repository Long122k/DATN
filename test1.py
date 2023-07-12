import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = {
    'Hotel Name': ['Hotel A', 'Hotel B', 'Hotel C', 'Hotel D', 'Hotel E'],
    'Price': [100, 150, 200, 120, 180],
    'Review Date': ['2023-06-01', '2023-06-02', '2023-06-03', '2023-06-04', '2023-06-05'],
    'Sentiment Score': [0.8, 0.6, 0.9, 0.7, 0.5],
    'Star Rating': [4, 3, 5, 4, 3],
    'Total Hotel Reviews': [500, 300, 1000, 800, 400]
}

df = pd.DataFrame(data)

# Bar chart: Average Price per Hotel
plt.figure(figsize=(8, 6))
plt.bar(df['Hotel Name'], df['Price'])
plt.xlabel('Hotel Name')
plt.ylabel('Price')
plt.title('Average Price per Hotel')
plt.show()

# Line chart: Sentiment Score over Time
df['Review Date'] = pd.to_datetime(df['Review Date'])  # Convert to datetime if not already in datetime format
plt.figure(figsize=(8, 6))
plt.plot(df['Review Date'], df['Sentiment Score'], marker='o')
plt.xlabel('Review Date')
plt.ylabel('Sentiment Score')
plt.title('Sentiment Score over Time')
plt.show()

# Pie chart: Star Rating Distribution
star_counts = df['Star Rating'].value_counts()
labels = star_counts.index
plt.figure(figsize=(8, 6))
plt.pie(star_counts, labels=labels, autopct='%1.1f%%')
plt.title('Star Rating Distribution')
plt.show()

# Number Card: Total Hotel Reviews
total_reviews = df['Total Hotel Reviews'].sum()
plt.figure(figsize=(4, 3))
plt.text(0.5, 0.5, str(total_reviews), fontsize=24, ha='center')
plt.axis('off')
plt.title('Total Hotel Reviews')
plt.show()
