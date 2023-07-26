import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website to scrape
base_url = "https://www.dubizzle.com.eg"
path = "/properties/apartments-duplex-for-sale/?filter=payment_option_eq_1"

# Number of pages to scrape
num_pages = 2500

# Lists to store the extracted data 
    
prices = []
locations = []
areas = []
times = []
subtitles = []
names = []
#bedrooms = []
#bathrooms = []

# Scrape the website
for page in range(1, num_pages + 80):
    url = base_url + path + "&page=" + str(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract the data
    price_tags = soup.find_all("div", class_="_1075545d _52497c97 _96d4439a")
    location_tags = soup.find_all("div", class_="e48cb10f undefined")
    area_tags = soup.find_all("div", class_="_1075545d _47c29360 _96d4439a")
    time_tags = soup.find_all("span", class_="c4ad15ab")
    subtitle_tags = soup.find_all("div", class_="_1075545d a8f6df88")
    name_tags = soup.find_all("div", class_="a5112ca8 _5fdf4379")
    """bedbed_tags = soup.find_all("span", class_="e05e3d9c")
    bathbath_tags = soup.find_all("span", class_="e05e3d9c")"""
    # Append the extracted data to the respective lists
    for tag in price_tags:
        prices.append(tag.get_text().strip())
    for tag in location_tags:
        locations.append(tag.get_text().strip())
    for tag in area_tags:
        areas.append(tag.get_text().strip())
    for tag in time_tags:
        times.append(tag.get_text().strip())
    for tag in subtitle_tags:
        subtitles.append(tag.get_text().strip())
    for tag in name_tags:
        names.append(tag.get_text().strip()) 
    """ for tag in bedbed_tags:
        bedrooms.append(tag.get_text().strip())
    for tag in bathbath_tags:
        bathrooms.append(tag.get_text().strip()) """           

# Create a DataFrame from the extracted data
data = {
    'Price': prices,
    'Location': locations,
    'Area': areas,
    'Time': times,
    'Subtitle': subtitles,
    'Name': names,
    #'Bedrooms': bedrooms,
    #'Bathrooms': bathrooms,
}
df = pd.DataFrame.from_dict(data, orient='index')
df = df.transpose()

# Save the DataFrame to a CSV file
df.to_csv('EgarHome.csv', index=False, encoding='utf-8-sig')

print("Data exported to scraped_data.csv file.")
