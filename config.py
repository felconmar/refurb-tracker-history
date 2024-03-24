from typing import Final


# https://refurb-tracker.com/feeds/es_in_ipad_iphone_ipod_homepod_imac_imacpro_macpro_macstudio_mini_macbookpro_macbookair_watch_atv_acc.xml
# https://refurb-tracker.com/feeds/es_in_all.xml
BASE_URL: Final = "https://refurb-tracker.com/feeds"
BASE_DIR: Final = "data"

# Supported countries
COUNTRIES: Final = [
    "au",
    "bx",
    "be",
    "ca",
    "xf",
    "cn",
    "de",
    "es",
    "fr",
    "hk",
    "ie",
    "it",
    "jp",
    "nl",
    "nz",
    "at",
    "pl",
    "sg",
    "kr",
    "cx",
    "ch",
    "tw",
    "uk",
    "us",
]

# Supported products (It is missing the tag 'all')
PRODUCTS: Final = [
    "ipad",
    "iphone",
    "ipod",
    "homepod",
    "imac",
    "imacpro",
    "macpro",
    "macstudio",
    "mini",
    "macbookpro",
    "macbookair",
    "watch",
    "atv",
    "acc",
]


def logMessage(message: str, file: str = None):
    print(message)
    if file:
        with open(file, "a+") as outfile:
            outfile.write(f"{message}\n")
