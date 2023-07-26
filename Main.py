import requests
from bs4 import BeautifulSoup
import pandas as pd

# Set the maximum number of pages to scrape
max_pages = 10

# Create empty lists to store the data
prices = []
subtitles = []
locations = []
times = []

# Iterate over each page up to the maximum number
for page in range(1, max_pages + 1):
    # Construct the URL for the current page
    url = f'https://www.dubizzle.com.eg/properties/?page={page}'

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Create a BeautifulSoup object from the response content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all the property elements on the page
        property_elements = soup.find_all('div', class_='sc-AxjAm')

        # Extract and store the data from each property element
        for property_element in property_elements:
            price_element = property_element.find('div', class_='_1075545d _52497c97 _96d4439a')
            subtitle_element = property_element.find('div', class_='_1075545d a8f6df88')
            location_element = property_element.find('div', class_='e48cb10f undefined') 
            time_element = property_element.find('div', class_='c4ad15ab')
        #time id c4ad15ab
            if price_element:
                prices.append(price_element.span.text.strip())
            else:
                prices.append('N/A')

            if subtitle_element:
                subtitles.append(subtitle_element.div.text.strip())
            else:
                subtitles.append('N/A')

            if location_element:
                locations.append(location_element.span.text.strip())
            else:
                locations.append('N/A')
            if time_element:
                    times.append(time_element.span.text.strip())
            else:
                times.append('N/A')
    else:
        print(f'Error: Failed to retrieve page {page}')

# Create a DataFrame from the extracted data
data = pd.DataFrame({'Price': prices, 'Subtitle': subtitles, 'Location': locations, 'Time': times})

# Save the DataFrame to a CSV file
data.to_csv('property_data.csv', index=False)
print('Data exported successfully!')
