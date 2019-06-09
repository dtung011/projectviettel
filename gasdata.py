from datetime import datetime, timedelta
from threading import Timer

x=datetime.today()
y = x.replace(day=x.day, hour=22, minute=0, second=0, microsecond=0) + timedelta(days=1)
delta_t=y-x

secs=delta_t.total_seconds()

def getgasdata():
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

    import openpyxl as op
    import datetime

    now = datetime.datetime.now()
    today = now.date()

    wb = op.load_workbook(r'C:\Users\pcjhi\OneDrive\Attachments\Desktop\Project Viettel\Data\gasdata.xlsx')
    ws = wb['gasdata']
    ws.append([today,gasprice])
    wb.save(r'C:\Users\pcjhi\OneDrive\Attachments\Desktop\Project Viettel\Data\gasdata.xlsx')
    wb.close()

t = Timer(secs, getusddata())
t.start()