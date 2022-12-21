from bs4 import BeautifulSoup
import requests
from fpdf import FPDF

'''Extracting the Table of contents from website'''
varsity_website ='https://zerodha.com/varsity/module/innerworth/'

source = requests.get(varsity_website).text
soup = BeautifulSoup(source,"lxml")

articles = soup.find_all('tr')
articles_list = []

'''Adding each article link to a list'''
for article in articles:
    articles_list.append((article.a).get('href'))
   
pdf = FPDF()
pdf.set_font("Arial", size = 12)

'''Iterating through each article'''
for website in articles_list:
    source = requests.get(website).text
    soup2 = BeautifulSoup(source,"lxml")

    '''Replacing some unicode character'''
    heading = soup2.find('h1',class_='large').text
    heading = (heading.replace(u"\u2018","'")
                    .replace(u"\u2013","'")
                    .replace(u"\u2019", "'")
                    .replace(u"\u2026", "...")
                    )

    contents = soup2.find('div','post')
    content =(contents.text
                    .replace(u"\U0001f642", "")
                    .replace(u"\u2019", "'")
                    .replace(u"\u201c", "-")
                    .replace(u"\u201d", "-")
                    .replace(u"\u2014", "'")
                    .replace(u"\u2018","")
                    .replace(u"\u2013","'")
                    .replace(u"\u2026", "...")
            )
    '''writing to a PDF file'''
    pdf.add_page()
    pdf.write(h=5.0,txt=f'{heading}.')
    pdf.write(h=5.0, txt='\n')
    pdf.write(h=5.0, txt=content)
    
'''Saving the PDF file'''
pdf.output("Zerodha.pdf")




