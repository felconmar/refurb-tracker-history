## Refurb Tracker Historic

You can access the historical data captured by this project through the GitHub Page available [here](https://felconmar.github.io/refurb-tracker-history/).

---

This project captures snapshots from the website [Refurb Tracker][refurb_tracker_url], maintaining a historical record of products available in the Refurb Apple Store across specific [countries](#Countries). The process retrieves RSS feeds for all countries and their product listings, saving new entries into CSV files tailored to each unique country-product combination. These records are updated hourly. Execution logs can be accessed in the `logs` directory. The entire process is automated using GitHub Actions.

[refurb_tracker_url]: https://refurb-tracker.com



### Countries:

* Australia
* Belgium
* Canada (English)
* Canada (French)
* China
* Germany
* Spain
* France
* Hong Kong (English)
* Ireland
* Italy
* Japan
* Netherlands
* New Zealand
* Austria
* Poland
* Singapore
* South Korea
* Switzerland
* Taiwan
* United Kingdom
* United States

### Products:

* iPad
* iPhone
* iPod
* HomePod
* iMac
* iMac Pro
* Mac Pro
* Mac Studio
* Mac mini
* MacBook Pro
* MacBook Air
* Apple Watch
* Apple TV
* Accessories

### License

This is a free and open-source project distributed under the GNU General Public License. This means you have the freedom to use, modify, and distribute the code, but you must also make the source code available under the same GPL license if you distribute a modified version.
