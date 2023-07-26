import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website to scrape
base_url = "https://www.dubizzle.com.eg"
path = "/properties/apartments-duplex-for-sale/?filter=down_payment_between_0_to_1"

# Number of pages to scrape
num_pages = 12

# Lists to store the extracted data
prices = []
locations = []
areas = []
times = []
subtitles = []

# Scrape the website
for page in range(1, num_pages + 1):
    url = base_url + path + "&page=" + str(page)
    response = requests.get(url)
    
    soup = BeautifulSoup(response.content, "html.parser", from_encoding="utf-8")

    # Extract the data
    price_tags = soup.find_all("div", class_="_1075545d _52497c97 _96d4439a")
    location_tags = soup.find_all("span", class_="e48cb10f undefined")
    area_tags = soup.find_all("span", class_="e021be12 _550213c9")
    time_tags = soup.find_all("span", class_="c4ad15ab")
    subtitle_tags = soup.find_all("div", class_="_1075545d a8f6df88")

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

# Create a DataFrame from the extracted data
data = {
    'Price': prices,
    'Location': locations,
    'Area': areas,
    'Time': times,
    'Subtitle': subtitles
}
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel('scraped_data.xlsx', index=False)

print("Data exported to scraped_data.xlsx file.")



# Set the maximum number of pages to scrape
"""max_pages = 2

# Create an empty list to store the prices
prices = []
locations = []
dates = [] 
subtitles = []


# Iterate over each page up to the maximum number
for page in range(1, max_pages + 1):
    # Construct the URL for the current page
    url = f'https://www.dubizzle.com.eg/properties/apartments-duplex-for-sale/?page={page}&filter=down_payment_between_0_to_1'

    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Create a BeautifulSoup object from the response content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all the property price elements on the page
        price_elements = soup.find_all('div', class_='_1075545d _52497c97 _96d4439a')
        Location_elements = soup.find_all('div', class_='e48cb10f undefined')
        date_elements = soup.find_all('div', class_='c4ad15ab')
        subtitle_elements = soup.find_all('div', class_='c4ad15ab')

        # Extract and store the prices
        for price_element in price_elements:
            price = price_element.span.text.strip()
            prices.append(price)
        else:
         print(f'Error: Failed to retrieve P page {page}')

        for location_element in Location_elements:
            location = location_element.span.text.strip()
            locations.append(location)  
    else:
        print(f'Error: Failed to retrieve L page {page}')

        for date_element in date_elements:
            date = date_element.span.text.strip()
            dates.append(date)   
        else:
            print(f'Error: Failed to retrieve D page {page}')

        for subtitle_element in subtitle_elements:
            subtitle = subtitle_element.span.text.strip()
            subtitles.append(subtitle)  
        else:  
            print(f'Error: Failed to retrieve S page {page}')
# Create a DataFrame from the extracted data
data = pd.DataFrame({'Prices': prices, 'Locations': locations, 'Dates': dates, 'Subtitles': subtitles})
df = pd.DataFrame.from_dict(data, orient='index')
df = df.transpose()


# Save the DataFrame to an XLSX file
data.to_excel('property_pricesww.xlsx', index=False)
print('Data exported successfully!')"""
