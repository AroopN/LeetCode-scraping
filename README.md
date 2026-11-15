# LeetCode Scraper

A Python and Selenium project that collected LeetCode problem ratings, difficulty, and acceptance data using Safari automation. Built in 2020, with the original CSV datasets included for exploration.

## Explore the data

- **[Dataset with problem names](leetcode_data_with_names.csv)** — problem URLs, names, likes, dislikes, like ratio, difficulty, accepted submissions, total submissions, and acceptance values.
- **[Original scraped dataset](leetcode_data.csv)** — the collected problem data.
- **[Recorded failures](errors.csv)** — indices of pages the original collection run failed to scrape.

These are historical snapshots. Ratings and submission counts reflect the original collection period.

## How it works

`main.py` starts Selenium’s Safari driver, opens the problem list, and visits the collected problem links. It writes successful results to `leetcode_data_partial.csv`, renames that file to `leetcode_data.csv` at the end, and records failed indices in `errors.csv`.

`update_names.py` is the companion script for adding problem names to the dataset.

## Current status

The scraper uses older Selenium APIs and LeetCode page selectors from 2020. Running it against today’s site requires updating those APIs and selectors. The included CSV files can be explored directly in a spreadsheet or with Python’s built-in `csv` module.

## Example

Run this from the repository directory to print the first five named records.

```python
import csv
from itertools import islice

with open("leetcode_data_with_names.csv", newline="", encoding="utf-8") as dataset:
    for problem in islice(csv.DictReader(dataset), 5):
        print(problem["NAME"], problem["DIFFICULTY"], problem["LIKES"])
```
