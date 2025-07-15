# summarize_data.py

import pandas as pd
from pathlib import Path


def main():
    # Load the cleaned CSV file
    df = pd.read_csv("samples/cleaned_listings.csv")

    # Generate basic stats
    total_listings = len(df)
    unique_categories = df["Category"].nunique()
    top_categories = df["Category"].value_counts().head(10)

    # Extract year from registration date
    df["Year Registered"] = pd.to_datetime(
        df["Date Registered"], errors='coerce').dt.year
    registrations_by_year = df["Year Registered"].value_counts().sort_index()

    # Approximate city names by taking the last token before state abbreviation
    city_series = df["Address"].str.extract(
        r",\s*(.*?)\s+[A-Z]{2}\s*\d{5}?")[0]
    top_cities = city_series.value_counts().head(10)

    # Build the report string
    report = []
    report.append("📊 Summary Report\n" + "─" * 30)
    report.append(f"📦 Total business listings: {total_listings}")
    report.append(f"🗂️ Unique categories: {unique_categories}\n")

    report.append("🏷️ Top 10 categories:")
    report.append(top_categories.to_string())
    report.append("\n📅 Registrations by Year:")
    report.append(registrations_by_year.to_string())

    report.append("\n🌆 Top 10 cities (approximate):")
    report.append(top_cities.to_string())

    # Combine all lines into final string
    summary_text = "\n\n".join(report)

    # Save plain text summary
    with open("output/summary.txt", "w") as f:
        f.write(summary_text)

    # Save markdown summary
    with open("samples/summary.md", "w") as f:
        f.write(summary_text)

    # Also print to terminal
    print(summary_text)


if __name__ == "__main__":
    main()
