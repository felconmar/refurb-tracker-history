import os

import pandas as pd
import feedparser


# https://refurb-tracker.com/feeds/es_in_ipad_iphone_ipod_homepod_imac_imacpro_macpro_macstudio_mini_macbookpro_macbookair_watch_atv_acc.xml


url = "https://refurb-tracker.com/feeds/es_in_all.xml"
feed = feedparser.parse(url)

# for entry in feed.entries:
#     print("Entry Id:", entry.id)
#     print("Entry Title:", entry.title)
#     print("Entry Date:", entry.updated)
#     print("Entry Link:", entry.link)
#     print("\n")

# print(feed.entries)


# Use pd.json_normalize to convert the JSON to a DataFrame
df = pd.json_normalize(feed.entries)
# Select the main columns
df = df[["updated", "title", "link"]]

# Rename the columns for clarity
df.columns = ["Date", "Title", "Link"]

# Display the DataFrame
# print(df)

# Store dataframe in csv file
df.to_csv("data/es/refurb_tracker_all.csv", index=False)
