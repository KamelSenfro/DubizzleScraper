# Dubizzle Web Scraper

This repository contains a web scraper for extracting data from the Dubizzle website, specifically for commercial properties for sale with a specified payment option.

## Overview

The script scrapes the following data from each listing:
- Price
- Location
- Area
- Time posted
- Subtitle
- Name of the advertiser

The scraped data is then saved into a CSV file for further analysis.

## Prerequisites

To run this scraper, you need to have Python and the required libraries installed. The necessary libraries are:
- `requests`
- `beautifulsoup4`
- `pandas`

You can install these libraries using `pip`:

```sh
pip install requests beautifulsoup4 pandas
