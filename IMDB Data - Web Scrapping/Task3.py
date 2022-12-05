import requests
import json
from bs4 import BeautifulSoup
r=requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
soup=BeautifulSoup(r.text,"html.parser")
def main():
    div=soup.find('div',class_='lister')
    tbody=div.find('tbody',class_='lister-list')
    trs=tbody.find_all('tr')
    rank_list=[];movie_name=[];release_year=[];ratings=[];urls=[]
    for tr in trs:
        ranks=tr.find('td',class_='titleColumn').get_text().strip()
        rank=''
        for i in ranks:
            if'.' not in i:
                rank=rank+i
            else:
                break
        rank_list.append(rank)
        name=tr.find('td',class_="titleColumn").a.get_text()
        movie_name.append(name)
        year=tr.find('td',class_="titleColumn").span.get_text()
        release_year.append(year)
        rating=tr.find('td',class_="ratingColumn imdbRating").strong.get_text()
        ratings.append(rating)
        link=tr.find('td',class_="titleColumn").a['href']
        movie_link="https://wwwimdb.com"+link
        urls.append(movie_link)
    movies_list=[]
    dictionary={}
    i=0
    while i<len(rank_list):
        dictionary["position"]=rank_list[i]
        dictionary["name"]=movie_name[i]
        dictionary["year"]=(release_year[i])
        dictionary["rating"]=ratings[i]
        dictionary["urls"]=urls[i]
        movies_list.append(dictionary.copy())      
        i+=1
        j=0
        p=[];g=[];h=[];z=[];v=[];b=[];c=[]
        q={}
        while j<len(movies_list):
            for x in movies_list[j]:
                if "(1959)" in movies_list[j][x] or "(1950)" in movies_list[j][x]or "(1951)" in movies_list[j][x]or "(1952)" in movies_list[j][x]or "(1953)" in movies_list[j][x]or "(1954)" in movies_list[j][x]or "(1955)" in movies_list[j][x]or "(1956)" in movies_list[j][x]or "(1957)" in movies_list[j][x]or "(1958)" in movies_list[j][x]:
                    g.append(movies_list[j])
                    q[1950]=g
                if "(1960)" in movies_list[j][x]or "(1961)" in movies_list[j][x]or "(1962)" in movies_list[j][x]or "(1963)" in movies_list[j][x]or "(1964)" in movies_list[j][x]or "(1965)" in movies_list[j][x]or "(1966)" in movies_list[j][x]or "(1967)" in movies_list[j][x]or "(1968)" in movies_list[j][x]or "(1969)" in movies_list[j][x]:
                    h.append(movies_list[j])
                    q[1960]=h
                if "(1970)" in movies_list[j][x]or "(1971)" in movies_list[j][x]or "(1972)" in movies_list[j][x]or "(1973)" in movies_list[j][x]or "(1974)" in movies_list[j][x]or "(1975)" in movies_list[j][x]or "(1976)" in movies_list[j][x]or "(1977)" in movies_list[j][x]or "(1978)" in movies_list[j][x]or "(1979)" in movies_list[j][x]:
                    z.append(movies_list[j])
                    q[1970]=z
                if "(1980)" in movies_list[j][x]or "(1981)" in movies_list[j][x]or "(1982)" in movies_list[j][x]or "(1983)" in movies_list[j][x]or "(1984)" in movies_list[j][x]or "(1985)" in movies_list[j][x]or "(1986)" in movies_list[j][x]or "(1987)" in movies_list[j][x]or "(1988)" in movies_list[j][x]or "(1989)" in movies_list[j][x]:
                    v.append(movies_list[j])
                    q[1980]=v
                if "(1990)" in movies_list[j][x]or "(1991)" in movies_list[j][x]or "(1992)" in movies_list[j][x]or "(1993)" in movies_list[j][x]or "(1994)" in movies_list[j][x]or "(1995)" in movies_list[j][x]or "(1996)" in movies_list[j][x]or "(1997)" in movies_list[j][x]or "(1998)" in movies_list[j][x]or "(1999)" in movies_list[j][x]:
                    b.append(movies_list[j])
                    q[1990]=b
                if "(2000)" in movies_list[j][x]or "(2001)" in movies_list[j][x]or "(2002)" in movies_list[j][x]or "(2003)" in movies_list[j][x]or "(2004)" in movies_list[j][x]or "(2005)" in movies_list[j][x]or "(2006)" in movies_list[j][x]or "(2007)" in movies_list[j][x]or "(2008)" in movies_list[j][x]or "(2009)" in movies_list[j][x]:
                    c.append(movies_list[j])
                    q[2000]=c
            j+=1
    with open("task3.json","w") as f:
        data=json.dump(q,f,indent=4)
main()