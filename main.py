import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

page = requests.get(url)

print(page.text)