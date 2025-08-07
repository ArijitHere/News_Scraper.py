# news_scraper.py

import requests
from bs4 import BeautifulSoup


url = 'https://www.bbc.com/news'
response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')


headlines = []

for item in soup.find_all('h3'):
    text = item.get_text(strip=True)
    if text and text not in headlines:
        headlines.append(text)


with open('headlines.txt', 'w', encoding='utf-8') as file:
    for line in headlines:
        file.write(line + '\n')

print(f"✅ {len(headlines)} headlines saved to 'headlines.txt'")
