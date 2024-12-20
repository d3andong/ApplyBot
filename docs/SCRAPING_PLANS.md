# Scraping Plans

## Overview
Scraping is now part of the MVP. We will start small, focusing on one job board (e.g., Indeed) to populate job listings. In the future, we’ll expand to other sources and improve reliability, proxy handling, and matching with user preferences.

## Initial Approach for MVP
1. **Single Source (Indeed):**
   - Use JobSpy or a custom scraper to fetch jobs for a specific role (e.g. "software engineer") and location from Indeed once daily.
   - Store results in a `jobs` table with fields like `title`, `company`, `location`, `is_remote`, `industries`, `date_posted`, `job_url`, `description`.

2. **Integration with Preferences:**
   - For MVP, filtering will be basic:  
     - If `work_arrangement='remote'`, show only remote jobs.  
     - Match roles by keyword search in `title` or `description`.  
     - Use location fields (city/state) to show relevant onsite jobs if `onsite` is chosen.
   - Over time, refine filtering logic and data normalization.

3. **Scraping Frequency:**
   - Once daily at a set time (e.g., midnight) to refresh listings.
   - If needed, add on-demand scraping triggered after user updates preferences (for MVP, this might be too complex—stick to daily refresh).

4. **Data Transformation:**
   - JobSpy returns a DataFrame. Convert it to JSON and map fields to our `jobs` schema.
   - Insert into `jobs` table, avoiding duplicates if possible.

5. **Future Enhancements:**
   - Add more boards (LinkedIn, Glassdoor, etc.) and handle rate limiting.
   - Integrate proxies and retry logic if blocked.
   - Enrich data (parse salary ranges, experience needed, etc.) to better match preferences.

6. **Relationship to Helper Flow:**
   - The scraped jobs fuel the helper flow by providing actual listings for the user to “practice” applying to.
   - Initially, we’ll pick a single job from the scraped list and show how GPT can assist in answering application questions.

7. **Fallback Plan:**
   - If JobSpy fails or is unreliable, consider writing a simple scraper with `requests` and `BeautifulSoup` or another tool.
   - Keep scraping logic modular so we can swap out the library easily.

## Timeline
- **MVP:**  
  - Implement daily scraping from Indeed for a single role and location.
  - Store results in DB and use them in `/jobs/eligible`.
  - Demonstrate at least one helper flow session using scraped job data.

- **Post-MVP:**
  - Add more sources.
  - Improve filtering and integration with preferences.
  - Consider real-time scraping on-demand if performance allows.

