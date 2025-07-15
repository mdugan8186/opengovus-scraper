# OpenGovUS Business Scraper

A Python web scraper that collects business registration data from [OpenGovUS - New York Businesses](https://opengovus.com/new-york-business). It uses Playwright for dynamic rendering, BeautifulSoup for parsing, and pandas for post-processing and analysis.

---

## 🚀 Features

- Extracts business name, address, category, and registration date
- Handles multiple pages via pagination
- Bypasses basic bot detection with stealth techniques
- Post-processes the data to check for duplicates and clean values
- Generates a plain-text and markdown summary of the dataset

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/mdugan8186/opengovus-scraper.git
cd opengovus-scraper
```

### 2. Install Python Dependencies

We recommend using Python 3.9+ and a virtual environment.

```bash
pip install -r requirements.txt
```

> You must also install Playwright dependencies and browser binaries:

```bash
playwright install
```

---

## 📦 Project Structure

```
opengovus-scraper/
├── script.py                # Main scraper
├── postprocess.py           # Data cleaning script
├── summarize_data.py        # Summary report generator
├── requirements.txt
├── output/                  # Raw output files (CSV, summary.txt)
│   └── opengovus_listings.csv
│   └── summary.txt
├── samples/                 # Cleaned and summarized data
│   └── cleaned_listings.csv
│   └── summary.md
└── extras/                  # Optional files: screenshots, raw HTML, etc.
```

---

## 🧪 How to Run

### 1. Scrape the Data

```bash
python script.py
```

This launches a **visible browser window** (not headless) to mimic real user behavior and avoid bot detection.

### 2. Clean the Data

```bash
python postprocess.py
```

Saves cleaned listings to `samples/cleaned_listings.csv`.

### 3. Generate a Summary Report

```bash
python summarize_data.py
```

Outputs plain text to `output/summary.txt` and markdown version to `samples/summary.md`.

---

## 📂 Output Format

CSV files contain the following columns:

- `Business Name`
- `Address`
- `Category`
- `Date Registered`

---

## 👤 Author

[Michael Dugan](https://github.com/mdugan8186)
