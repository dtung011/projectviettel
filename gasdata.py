
import time

def gasdata():    
    import requests

    url = "https://webgia.com/gia-xang-dau/petrolimex/"

    response = requests.get(url)
    text = response.content.decode("utf8")

    ##################################

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(text, "html.parser")

    gaspricelist= soup.find('table', class_='table table-bordered table-hover').find_all('td')
    gasprice = float(gaspricelist[2].get_text().replace(',',''))
    print(gasprice)

    ##################################

    import pandas as pd
    import datetime

    now = datetime.datetime.now()
    today = now.date()
    print(today)
    f = pd.read_csv("Data\generaldata.csv")
    f = f.append({'order':len(f)+1, 'date':today, 'gas':gasprice}, ignore_index=True)
    f.to_csv("Data\generaldata.csv", index = False, encoding = 'utf8')


