# Testing – OpenGovUS Business Scraper

## Render → Extract → Clean → Summarize (manual flow)
1. **Run the scraper**
   ```bash
   python script.py
   ```
   - Confirms Playwright launches and pages render
   - Expects `output/opengovus_listings.csv` to be created

2. **Post-process (clean & sort)**
   ```bash
   python postprocess.py
   ```
   - Loads `output/opengovus_listings.csv`
   - Dedupes, normalizes, converts dates, sorts by `Date Registered`
   - Saves `samples/cleaned_listings.csv`

3. **Summarize dataset**
   ```bash
   python summarize_data.py
   ```
   - Loads `samples/cleaned_listings.csv`
   - Writes `output/summary.txt` and `samples/summary.md`

---

## Sanity Checks
- [ ] `python -m playwright install chromium` completes successfully
- [ ] `output/opengovus_listings.csv` exists and is non-empty
- [ ] Cleaned CSV saved to `samples/cleaned_listings.csv`
- [ ] Summary files written to `output/summary.txt` and `samples/summary.md`

## Data Quality
- [ ] Columns present: `Business Name`, `Address`, `Category`, `Date Registered`
- [ ] No duplicate rows
- [ ] `Date Registered` parses to datetime without widespread `NaT`
- [ ] Reasonable distribution of categories (spot-check top counts)

## Selector & Site Maintenance
- [ ] If site layout changes, update selectors in `script.py`
- [ ] Re-run steps 1–3 and validate outputs
- [ ] Consider moving selectors into a `config/` JSON for easier updates (future enhancement)

## Troubleshooting
- **Empty CSV**: Check selectors (inspect page, re-run headed mode), ensure pagination is working
- **HTTP 429 / blocking**: Add delays/jitter between pages; reduce concurrency
- **Encoding issues**: Open CSV in a text editor and confirm UTF-8; use `errors='ignore'` if needed during reads
