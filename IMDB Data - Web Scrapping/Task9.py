from textwrap import indent
import requests
import json
from bs4 import BeautifulSoup
rel=requests.get("https://www.imdb.com/title/tt0066763/")
soup=BeautifulSoup(rel.content,"html.parser")
con=soup.find('script',type='application/ld+json').text
a=json.loads(con)

with open("task9.json",'w')as f:
    json.dump(a,f,indent=10)