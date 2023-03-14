import requests
from bs4 import BeautifulSoup

# URL of the Reliance Industries stock page on Moneycontrol
url = "https://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    print(f"Error: Request returned status code {response.status_code}")
    exit()

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the element that contains the stock price and extract the price text
price_element = soup.find("span", class_="lastprice")

# Check if the element was found
if price_element is None:
    print("Error: Could not find price element")
    exit()

price = price_element.text.strip()

print("Reliance Industries stock price: ", price)
