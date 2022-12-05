# import requests
# import json
# from bs4 import BeautifulSoup
# rel=requests.get("https://www.imdb.com/india/top-rated-indian-movies")
# soup=BeautifulSoup(rel.content,"html.parser")
# movies=soup.find("tbody",class_="lister-list",).find_all("tr")
# list=[]
# for movie in movies:
#     dic={"movie":"","year":"","rating":"","position":"","link":""}
#     name=movie.find('td',class_="titleColumn").a.text
#     ratings=movie.find('td',class_="ratingColumn imdbRating").strong.text
#     position=movie.find("td",class_='titleColumn').get_text(strip=True).split('.')[0]
#     year=movie.find('td',class_="titleColumn").span.text.strip("()")

#     url=movie.find("td",class_="titleColumn").a["href"]
#     link="https://ww.imdb.com/"+url

#     dic["movie"]=name
#     dic["year"]=year
#     dic["rating"]=ratings
#     dic["position"]=position
#     dic["link"]=link
#     list.append(dic)

# answer={}
# a=[]
# b=[]
# c=[]
# d=[]
# i=0
# while i<len(list):
#     if list[i]["year"]>="1960" and list[i]["year"]<="1969":
#         a.append(list[i])
#         answer["1960"]=a
#     if list[i]["year"]>="1970" and list[i]["year"]<="1979":
#         b.append(list[i])
#         answer["1970"]=b
#     if list[i]["year"]>="1980" and list[i]["year"]<="1989":
#         c.append(list[i])
#         answer["1980"]=c

#     if list[i]["year"]>="2000" and list[i]["year"]<="2009":
#         d.append(list[i])
#         answer["2000"]=d
#     i+=1

# with open("task2.json","w")as f:
#     json.dump(answer,f,indent=8)


import requests 
from bs4 import BeautifulSoup
import json
req = requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
soup=BeautifulSoup(req.content,'html.parser')
# print(soup.prettify())
movies=soup.find('tbody',class_='lister-list').find_all('tr')
name_list=[]
year_list=[]
dic=[]
# link_url=[]
for movie in movies:
        list={"movie":"","position":"","rating":"","year":"","link":""}
        name=movie.find('td',class_='titleColumn').a.text
        position=movie.find('td',class_='titleColumn').get_text(strip=True)
        year=movie.find('td',class_='titleColumn')
        # year_list.append(year)
   
        rating=movie.find('td',class_='ratingColumn imdbRating').strong.text
        link=movie.find('td',class_='titleColumn').a['href']
        movie_link="https://www.imdb.com"+link
               
        # link_url.append(movie_link)
        list["movie"]=name
        list["position"]=position
        list["rating"]=rating
        list["link"]=movie_link
        name_list.append(list)
        dic.append(list)
with open("task2.json","w")as f:
    json.dump(dic,f,indent=8)