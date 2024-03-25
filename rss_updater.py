import os
from pathlib import Path
import datetime

import pandas as pd
import feedparser

from config import BASE_URL, BASE_DIR, COUNTRIES, PRODUCTS, logMessage


def process_feed(country, product, base_dir, base_url, log_file):
    dir = Path(base_dir) / country
    url = f"{base_url}/{country}_in_{product}.xml"
    target_csv = dir / f"refurb_tracker_{product}.csv"

    # Read the rss feed
    feed = feedparser.parse(url)
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

        # Log new inserts
        new_items = len(df.index) - len(df_old.index)
        msg = f"Country: {country}, product: {product} --> new items: {new_items}"
        logMessage(msg, log_file)


def main():
    # Log file creation
    log_file_name = "RSSUpdaterRun-{date:%Y%m%d_%H%M%S}.log".format(
        date=datetime.datetime.now()
    )
    log_file = Path("logs") / f"{log_file_name}"
    # Iterate through countries and products
    for country in COUNTRIES:
        for product in PRODUCTS:
            process_feed(country, product, BASE_DIR, BASE_URL, log_file)


if __name__ == "__main__":
    main()
