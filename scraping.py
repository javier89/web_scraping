import requests
from bs4 import BeautifulSoup

#url = "http://sirh.sazacatecas.gob.mx/login/"
url = "http://quotes.toscrape.com/"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.find_all('h1'))

print(soup.find_all('div', {'class':'tags'}))

tags = soup.find_all(class_="tags")
lst = []
for tag in tags:
    lst.append(tag.text.replace("\n", " ").strip())
    lst2 = [tag.replace(" ", "") for tag in lst]
    print(lst2)
