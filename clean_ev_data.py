import pandas as pd

# 1️⃣ Load dataset
df = pd.read_csv('Ev_raw_dataset.csv')
print("✅ Dataset loaded successfully!")
print(f"Shape before cleaning: {df.shape}")
print("\nColumns:", list(df.columns))

# 2️⃣ Check for missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# 3️⃣ Drop duplicate rows
df = df.drop_duplicates()
print("\n✅ Duplicates removed.")

# 4️⃣ Drop rows with missing key values
# (You can change column names as per your dataset)
important_columns = ['Price_USD', 'Range_km', 'Battery_kWh']
for col in important_columns:
    if col in df.columns:
        df = df.dropna(subset=[col])

print("\n✅ Dropped rows with missing important values.")

# 5️⃣ Fill or fix other missing values
df = df.fillna({
    'Brand': 'Unknown',
    'Country': 'Unknown'
})
print("\n✅ Filled missing text columns.")

# 6️⃣ Remove outliers (optional but recommended)
if 'Price_USD' in df.columns:
    Q1 = df['Price_USD'].quantile(0.25)
    Q3 = df['Price_USD'].quantile(0.75)
    IQR = Q3 - Q1
    df = df[(df['Price_USD'] >= Q1 - 1.5*IQR) & (df['Price_USD'] <= Q3 + 1.5*IQR)]
    print("\n✅ Outliers in price removed.")

# 7️⃣ Remove extra spaces and clean text columns
text_cols = df.select_dtypes(include='object').columns
for col in text_cols:
    df[col] = df[col].str.strip()

print("\n✅ Cleaned text columns.")

# 8️⃣ Save cleaned dataset
df.to_csv('cleaned_ev_data.csv', index=False)
print("\n🎉 Cleaning complete! Saved as 'cleaned_ev_data.csv'")
print(f"Shape after cleaning: {df.shape}")
