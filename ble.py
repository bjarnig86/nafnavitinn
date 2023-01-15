import requests
from bs4 import BeautifulSoup

r = requests.get("https://attavitinn.is/samfelagid/merkingar-nafna/")

soup = BeautifulSoup(r.content, features='html.parser') 

rows = soup.find_all('div', id="name-wraper")

print(len(rows))

for row in rows:
    h3 = row.find_all('h3')
    p = row.find_all('p')
    for i in range(len(h3)):
        print(h3[i].text.strip())
        print(p[i].text.strip())