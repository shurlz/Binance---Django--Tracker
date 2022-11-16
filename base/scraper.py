import requests
from bs4 import BeautifulSoup

resource = requests.get("https://www.binance.com/en/markets").text

soup = BeautifulSoup(resource, 'lxml')

names = soup.find_all('div', class_='css-1ap5wc6')
symbols = soup.find_all('div', class_='css-1x8dg53')
prices = soup.find_all('div', class_='css-ovtrou')
changes = soup.find_all('div', class_='css-1ca67uc')
volumes = soup.find_all('div', class_='css-102bt5g')
market_caps = soup.find_all('div', class_='css-s779xv')

names = [name.text for name in names]
symbols = [symbol.text for symbol in symbols]
prices = [price.text for price in prices]
changes = [change.text for change in changes]
volumes = [volume.text for volume in volumes]
market_caps = [market_cap.text for market_cap in market_caps]

def binance_scraper():
    all_values = {"names":names, "symbols":symbols, "prices":prices, "changes":changes, "volumes":volumes, "market_caps":market_caps}
    return all_values

