from bs4 import BeautifulSoup
import requests
import csv

#res = requests.get("http://quotes.toscrape.com/")
#soup = BeautifulSoup(res.text, 'html.parser')

# Encontrar la longitud de la pagina
#length  = len(soup.select(".text"))

# Raspado de todas las citas con el nombre del autor 
#for i in range(0, length):
#    quote = soup.select(".text")[i].get_text().strip()
#    author = soup.select('.author')[i].get_text().strip()
#    print(quote)
#    print(author)

# Descubrimiento de cotizaciones de todas las paginas
page = 10 
for i in range(0, page):
    res = requests.get(f"http://quotes.toscrape.com/page/{i}/")
    soup = BeautifulSoup(res.text, "html.parser")

    #Encontrar la longitud de la pagina
    length = len(soup.select(".text"))
    
    #Raspando todas las citas con el nombre del author
    for j in range(0, length):
        quote = soup.select(".text")[j].get_text().strip()
        quote = quote.replace("\u2032"," ")
        author = soup.select('.author')[i].get_text().strip()
        with open('quote.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([quote, author])

print("Done!")
