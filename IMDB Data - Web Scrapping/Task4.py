import requests
import json
from bs4 import BeautifulSoup
rel=requests.get("https://www.imdb.com/title/tt0066763/")
soup=BeautifulSoup(rel.content,"html.parser")
con=soup.find('script',type='application/ld+json').text
a=json.loads(con)
# print(a)
dic={}
# print(a)
for i in a:
    dic['name']=a['name']
    dic['director']=[a['director'][0]['name']]
    dic['image']=a['image']
    dic['bio']=a['description']
    # dic['runtime']=a['runtime']
    dic["language"]=a['review']['inLanguage']
    dic['genre']=a['genre']
    dic['country']='india'
    # print(dic)
with open("task4.json","w") as f:
    json.dump(dic,f,indent=8)