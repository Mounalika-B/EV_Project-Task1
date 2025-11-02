import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("cleaned_ev_data.csv")
print("✅ Dataset Loaded Successfully!")
print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nSample Data:\n", df.head())

# Check for missing values
print("\n🔹 Missing Values:\n", df.isnull().sum())

# Check numeric summary
print("\nSummary Statistics:\n", df.describe())

# Correlation heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(numeric_only=True), annot=False, cmap='coolwarm')
plt.title("Feature Correlation Heatmap")
plt.show()

# Relationship examples
sns.scatterplot(x='range_km', y='price_usd', data=df)
plt.title('Range vs Price')
plt.show()

sns.barplot(x='manufacturer', y='price_usd', data=df.head(50))
plt.title('Manufacturer vs Price')
plt.show()

# 1️⃣ Distribution of Price
plt.figure(figsize=(7,5))
sns.histplot(df['price_usd'], bins=30, kde=True)
plt.title('EV Price Distribution')
plt.xlabel('Price (USD)')
plt.ylabel('Count')
plt.show()

# 2️⃣ Top 10 Manufacturers
plt.figure(figsize=(8,5))
top_manu = df['manufacturer'].value_counts().head(10)
sns.barplot(x=top_manu.index, y=top_manu.values, palette='viridis')
plt.title('Top 10 EV Manufacturers')
plt.xlabel('Manufacturer')
plt.ylabel('Number of Models')
plt.xticks(rotation=45)
plt.show()


# 4️⃣ Range vs Battery Capacity
plt.figure(figsize=(7,5))
sns.scatterplot(x='battery_kwh', y='range_km', data=df, hue='fuel_type')
plt.title('Battery Capacity vs Range')
plt.xlabel('Battery (kWh)')
plt.ylabel('Range (km)')
plt.legend()
plt.show()

# 5️⃣ Average Price by Country
plt.figure(figsize=(10,5))
avg_price = df.groupby('country')['price_usd'].mean().sort_values(ascending=False).head(10)
sns.barplot(x=avg_price.index, y=avg_price.values, palette='plasma')
plt.title('Average EV Price by Country')
plt.ylabel('Average Price (USD)')
plt.xlabel('Country')
plt.xticks(rotation=45)
plt.show()

print("\n✅ EDA Completed Successfully!")

