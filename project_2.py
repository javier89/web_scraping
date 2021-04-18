import requests
from bs4 import BeautifulSoup

sidebar = []

res = requests.get("https://www.tutorialspoint.com/cprogramming/index.htm")
soup = BeautifulSoup(res.text, "html.parser")

for i in range(0, len(soup.select(".chapters a"))):
    sidebar_text = soup.select(".chapters a")[i].getText().strip()
    sidebar_text = sidebar_text.replace("-","_").lower()
    sidebar.append(sidebar_text)

sidebar = sidebar[1:]
sidebar[0] = "index"
page = sidebar[2]
content = ""

for i in range(0, len(sidebar)):
    page = sidebar[i]
    page = page.replace("","_")
    url = f"https://www.tutorialspoint.com/cprogramming/{page}.htm"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    data = soup.select("h2, p")

    for i in range(0, len(data)):
        content = content + (data[i].getText())
        content = content+"\n"
        content = content.replace("\u2212", " ")
        content = content.replace("\u2192"," ")
    f = open("c_notes_tutorial_points.txt", "a")
    f.write(content)
    print(content)
    f.close()
