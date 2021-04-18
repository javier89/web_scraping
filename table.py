import requests
from bs4 import BeautifulSoup
import csv

url = 'https://webscraper.io/test-sites/tables'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

table = soup.select('.table')[0]
table_header = table.find('thead').find_all('th')
with open('table.csv', 'a', newline='') as f:
    write = csv.writer(f)
    header = []
    for th in table_header:
        header.append(th.text)
    write.writerow(header)
    for row in table.find_all('tr'):
        body = []
        for data in row.find_all('td'):
            body.append(data.text)
            print(body)
        write.writerow(body)

