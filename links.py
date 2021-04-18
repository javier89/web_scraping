import requests
from bs4 import BeautifulSoup

url = "https://metals-mx.myshopify.com/"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

for a_tag in soup.findAll("a"):
    href = a_tag.attrs.get("href")
    if href != "":
        print(href)
        continue

div = soup.find('div',{'class':'col-sm-4 col-lg-4 col-md-4'})
a = div.find('a')
link = a.attrs.get("href")
print(link)

