from datetime import datetime, timedelta
from threading import Timer

x=datetime.today()
y = x.replace(day=x.day, hour=22, minute=0, second=0, microsecond=0) + timedelta(days=1)
delta_t=y-x

secs=delta_t.total_seconds()

def getoildata():
    import requests

    url = "https://oilprice.com/"

    response = requests.get(url)
    text = response.content.decode("utf8")

    ##################################

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(text, "html.parser")
    oilprice= float(soup.find('td', class_='value').get_text())
    print(oilprice)

    ##################################

    import openpyxl as op
    import datetime

    now = datetime.datetime.now()
    today = now.date()

    wb = op.load_workbook(r'C:\Users\pcjhi\OneDrive\Attachments\Desktop\Project Viettel\Data\oildata.xlsx')
    ws = wb['oildata']
    ws.append([today,oilprice])
    wb.save(r'C:\Users\pcjhi\OneDrive\Attachments\Desktop\Project Viettel\Data\oildata.xlsx')
    wb.close()

t = Timer(secs, getoildata())
t.start()