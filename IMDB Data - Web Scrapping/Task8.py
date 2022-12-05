import requests
import json
from bs4 import BeautifulSoup
rel=requests.get("https://www.imdb.com/title/tt0066763/")
soup=BeautifulSoup(rel.content,"html.parser")
con=soup.find('script',type='application/ld+json').text
a=json.loads(con)
l={}
for key in a:
    if key=="url":
        p=a[key]
        l['id']=p
print(l)