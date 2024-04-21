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
            new_items = len(df.index) - len(df_old.index)
        else:
            df = df_new
            new_items = len(df.index)

        # Store to target csv
        df.to_csv(target_csv, index=False)

        if new_items != 0:
            # Log new inserts
            msg = f"Country: {country}, product: {product} --> new items: {new_items}"
            logMessage(msg, log_file)

def check_log_file(log_file_path):
    try:
        with open(log_file_path, 'r') as file:
            lines = file.readlines()
            last_line = lines[-1].strip()
            if last_line.startswith("Date: "):
                return True
            else:
                return False
    except FileNotFoundError:
        print("Log file not found.")


def main():
    date=datetime.datetime.now()
    # Log file creation
    log_file_name = "RSSUpdaterRun-{date:%Y%m}.log".format(
        date=date
    )
    log_file = Path("logs") / f"{log_file_name}"

    # Date initial message for logs
    date_msg = "Date: {date:%Y/%m/%d %H:%M:%S}".format(
        date=date
    )
    logMessage(date_msg, log_file)

    # Iterate through countries and products
    for country in COUNTRIES:
        for product in PRODUCTS:
            process_feed(country, product, BASE_DIR, BASE_URL, log_file)

    # Log that there are no entires if aplicable.
    if check_log_file(log_file):
        no_entries_msg = "No new entries."
        logMessage(no_entries_msg, log_file)

    # Date separator message
    end_msg = "-" * 60 
    logMessage(end_msg, log_file)


if __name__ == "__main__":
    main()
