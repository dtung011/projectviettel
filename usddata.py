import requests

url = "https://vn.investing.com/currencies/usd-vnd-historical-data"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

response = requests.get(url, headers=headers)
text = response.content.decode("utf8")

##################################

from bs4 import BeautifulSoup
soup = BeautifulSoup(text, "html.parser")

exchangerate = float(soup.find('span', class_='arial_26 inlineblock pid-2214-last').get_text().replace(',',''))
print(exchangerate)

#################################

import pandas as pd 
with open('my_csv.csv', 'a') as f:
    df.to_csv()

