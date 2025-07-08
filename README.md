# OpenGovUS NY Business Listings Scraper

This project is a Python-based web scraper that extracts business registration listings from the [OpenGovUS New York Business page](https://opengovus.com/new-york-business). It uses Playwright with stealth tactics to bypass basic bot detection, and saves structured business data to a CSV file.

---

## 🔍 What It Does

- Navigates through paginated business listings.
- Scrapes the following information for each business:
  - **Business Name**
  - **Address**
  - **Category**
  - **Date Registered**
- Follows all "Next Page" links until pagination ends.
- Outputs the results to a CSV file (`opengovus_listings.csv` by default).

---

## ⚙️ Installation

First, make sure Python 3.7+ is installed. Then:

```bash
# Clone the repository
git clone https://github.com/yourusername/opengovus_scraper.py.git
cd opengovus_scraper.py

# Install dependencies
pip install playwright beautifulsoup4

# Install Playwright browser drivers
playwright install
```

---

## 🚀 How to Run

```bash
python script.py
```

The scraper will:

1. Open the website using Playwright.
2. Apply stealth techniques.
3. Visit each page and extract listings.
4. Save everything into `opengovus_listings.csv`.

> 💡 The browser runs in non-headless mode so you can monitor behavior. To change the delay or headless setting, modify the `get_rendered_html()` function.

---

## 📄 Output Format

The CSV file will include:

| Business Name              | Address                              | Category                    | Date Registered |
| -------------------------- | ------------------------------------ | --------------------------- | --------------- |
| Wakefield & Associates...  | Calle 50 Piso 32 Global Bank, Panama | Debt Collection Agency      | 2023-07-21      |
| Inder Multani Construction | 8906 241st St, Bellerose, NY 11426   | Home Improvement Contractor | 2023-07-21      |
| ...                        | ...                                  | ...                         | ...             |

---

## 🔧 Tools & Libraries Used

- **[Playwright](https://playwright.dev/)** – browser automation
- **[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)** – HTML parsing
- **Python Standard Libraries**: `csv`, `time`, `random`, `urllib.parse`

---

## 📌 Sample Use Case

This project can be used to:

- Build a dataset of newly registered businesses
- Analyze trends in business types or registration dates
- Feed data into a lead-generation pipeline for local services

---

## 👤 Author

Michael Dugan  
[GitHub](https://github.com/mdugan8186)
