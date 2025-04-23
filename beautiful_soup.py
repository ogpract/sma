# pip install beautifulsoup4 requests


import requests
from bs4 import BeautifulSoup

# Set the target URL (example: blog site or product listings)
url = "https://quotes.toscrape.com/"

# Send HTTP GET request
response = requests.get(url)

# Check for successful response
if response.status_code == 200:
    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: Collect all quote texts
    quotes = soup.find_all('span', class_='text')
    
    print("Collected Quotes:\n")
    for i, quote in enumerate(quotes, 1):
        print(f"{i}. {quote.text}")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
