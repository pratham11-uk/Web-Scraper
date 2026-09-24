from bs4 import BeautifulSoup # for making structured tree into python objects for easy access.
import requests # requests and downloads raw unstructured html in form of strings.
# lxml converts a structured html tree from data given by request which is then used by BS.
import csv

request = requests.get('https://www.scrapethissite.com/pages/simple/').text
# request is raw text

soup = BeautifulSoup(request,'lxml') # structured heirarchical tree is been constructed (soup object)
# soup = soup.prettify() don not use as it makes soup object to plain string

countries= open('country.csv' , 'w',encoding='utf-8')
csv_writer=csv.writer(countries)
csv_writer.writerow(['country name','capital','population','area'])


for country in soup.find_all('div','col-md-4 country'):
    try:
        country_name = country.h3.text.strip() # this is how u access deep 
    except:
        country_name = None # let in case website is corrupted

    try:
        capital = country.find('div',class_='country-info').find('span',class_='country-capital').text
    except:
        capital = None

    try:
        population = country.find('div',class_='country-info').find('span',class_='country-population').text
    except:
        population = None

    try:
        area = country.find('div',class_='country-info').find('span',class_='country-area').text
    except:
        area=None
    csv_writer.writerow([country_name,capital,population,area])






    