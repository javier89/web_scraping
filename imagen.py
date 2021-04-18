from bs4 import BeautifulSoup
import requests
import os

res = requests.get(f"https://www.shutterstock.com/search/fruit")
soup = BeautifulSoup(res.text,"html.parser")
links = []
print(soup)


images = []
tags = soup.findAll("img")
for link in tags:
  src = link.attrs.get('src')
  if str(src)!="None":
     link = link.attrs.get('src')
     links.append(link)
print(links)
image_count=1
for image in links:
  with open('image_'+str(image_count)+'.jpg', 'wb') as f:
    res = requests.get(image)
    f.write(res.content)
    image_count+=1
    print("Saving image_"+str(image_count))
