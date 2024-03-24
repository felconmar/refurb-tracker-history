import os
from pathlib import Path

import pandas as pd
import feedparser

from config import BASE_URL, BASE_DIR, COUNTRIES, PRODUCTS


def process_feed(country, product, base_dir, base_url):
    dir = Path(base_dir) / country
    url = f"{base_url}/{country}_in_{product}.xml"
    target_csv = dir / f"refurb_tracker_{product}.csv"

    feed = feedparser.parse(url)

    # Read the rss feed
    df_new = pd.json_normalize(feed.entries)

    # Select and rename columns if dataframe is not empty
    if not df_new.empty:
        df_new = df_new[["updated", "title", "link"]]
        # Rename columns
        df_new.columns = ["Date", "Title", "Link"]

        # If there is already a csv file in the target location, insert new.
        if target_csv.exists():
            df_old = pd.read_csv(target_csv)
            df = pd.concat([df_old, df_new]).drop_duplicates()
        else:
            df = df_new

        # Store to target csv
        df.to_csv(target_csv, index=False)


# Iterate through countries and products
for country in COUNTRIES:
    for product in PRODUCTS:
        process_feed(country, product, BASE_DIR, BASE_URL)
