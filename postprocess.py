import pandas as pd

# Load the raw scraped data
df = pd.read_csv("output/opengovus_listings.csv")

# Basic info
print("🧠 Data Overview:")
print(df.info())

# Preview first few rows
print("\n👀 First 5 rows:")
print(df.head())

# Check for duplicates
duplicate_count = df.duplicated().sum()
print(f"\n🔁 Duplicate rows: {duplicate_count}")

# Check for missing values
missing_counts = df.isnull().sum()
print("\n🚫 Missing values per column:")
print(missing_counts)

# Convert 'Date Registered' to datetime
df['Date Registered'] = pd.to_datetime(df['Date Registered'], errors='coerce')

# Sort by date descending
df = df.sort_values(by='Date Registered', ascending=False)

# Save cleaned version
df.to_csv("samples/cleaned_listings.csv", index=False)

print("\n✅ Cleaned and saved as cleaned_listings.csv")
