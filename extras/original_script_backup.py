from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import csv
import time
import random
from urllib.parse import urlparse, parse_qs, urlunparse


def stealth_hacks(page):
    """Apply manual stealth tactics to avoid bot detection."""
    page.evaluate("""
        () => {
            Object.defineProperty(navigator, 'webdriver', { get: () => false });
            window.chrome = { runtime: {} };
            Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] });
            Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5] });
        }
    """)


def get_rendered_html(url, delay=2000):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print(f"🌐 Navigating to page: {url}")
        page.goto(url, wait_until="load")

        stealth_hacks(page)
        page.wait_for_timeout(delay)

        html = page.content()
        browser.close()
        return html


def extract_listings(html):
    soup = BeautifulSoup(html, "html.parser")

    # More precise selector for the business listings table
    table = soup.select_one(
        "table.table-hover.table-condensed.table-sm.table-responsive.table-striped")

    if not table:
        print("❌ Table not found.")
        return []

    print("✅ Correct table found.")
    listings = []

    rows = table.select("tr")
    print(f"Found {len(rows)} rows (including header).")

    for i, row in enumerate(rows[1:], 1):  # Skip header
        cols = row.select("td")
        print(f"Row {i} has {len(cols)} columns.")

        if len(cols) == 4:
            listings.append({
                "Business Name": cols[0].text.strip(),
                "Address": cols[1].text.strip(),
                "Category": cols[2].text.strip(),
                "Date Registered": cols[3].text.strip()
            })

    return listings


def save_to_csv(listings, filename="opengovus_listings.csv"):
    if not listings:
        print("⚠️ No listings to save.")
        return

    keys = listings[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(listings)

    print(f"💾 Saved {len(listings)} listings to {filename}")


def extract_next_page_url(html):
    """Extract the next page URL from pagination controls."""
    soup = BeautifulSoup(html, "html.parser")
    pagination = soup.select_one("ul.pagination")

    if pagination:
        print("📎 Pagination block found.")
        next_link = pagination.find("a", string="Next Page")
        if next_link:
            print("➡️ Next page link found:", next_link["href"])
            return next_link["href"]
        else:
            print("⛔ No 'Next Page' link found.")
    else:
        print("❌ Pagination block not found.")
    return None


def normalize_url(url):
    parsed = urlparse(url)
    query = parse_qs(parsed.query)

    # Remove 'page=1' if it's explicitly there
    if query.get('page') == ['1']:
        query.pop('page')

    # Reconstruct query string
    new_query = '&'.join(f"{k}={v[0]}" for k, v in query.items())

    normalized = parsed._replace(query=new_query)
    return urlunparse(normalized)


def scrape_all_pages(start_url):
    current_url = start_url
    all_listings = []
    visited_urls = set()
    page_num = 1

    while current_url:
        normalized = normalize_url(current_url)
        if normalized in visited_urls:
            print("🔁 Duplicate page detected. Stopping.")
            break
        visited_urls.add(normalized)

        print(f"🔄 Scraping page {page_num}: {current_url}")
        html = get_rendered_html(current_url)
        listings = extract_listings(html)
        all_listings.extend(listings)
        print(f"✅ Extracted {len(listings)} listings from page {page_num}")

        next_page = extract_next_page_url(html)
        if next_page and not next_page.startswith("http"):
            next_page = "https://opengovus.com" + next_page

        current_url = next_page
        page_num += 1

        time.sleep(random.uniform(1.5, 4.0))

    return all_listings


def main():
    start_url = "https://opengovus.com/new-york-business"
    all_listings = scrape_all_pages(start_url)
    save_to_csv(all_listings)


if __name__ == "__main__":
    main()
