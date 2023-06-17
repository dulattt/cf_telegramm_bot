import requests
from bs4 import BeautifulSoup as BS
import json


URL = "https://codeforces.com/contests"
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}


def get_html(url: str, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def content(html) -> list:
    soup = BS(html, 'html.parser')
    items = soup.find('div', class_='datatable')

    data = []
    table = items.find('table')
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    return data


def main() -> None:
    html = get_html(URL)
    my_data = content(html.text)

    with open("data.json", "w") as file:
        json.dump(my_data, file)
