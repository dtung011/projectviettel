from datetime import datetime, timedelta
from threading import Timer

x=datetime.today()
y = x.replace(day=x.day, hour=22, minute=0, second=0, microsecond=0) + timedelta(days=1)
delta_t=y-x

secs=delta_t.total_seconds()

def getusddata():   
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
    data = pd.read_csv(r'C:\Users\pcjhi\OneDrive\Attachments\Desktop\Project Viettel\Data\generaldata.csv')

t = Timer(secs, getusddata())
t.start()