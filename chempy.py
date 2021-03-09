import requests
from bs4 import BeautifulSoup

def solve(reaction1, reaction2):  
    url = 'https://chemequations.com/ru/?s=' + reaction1 + '+%2B+' + reaction2
    
    page = requests.get(url)

    soup = BeautifulSoup(page.text, "html.parser")

    equation = soup.findAll('h1', class_='equation main-equation well')
    
    for data in equation:
        return data.text

def info(lang, compound):
    url = 'https://chemequations.com/' + lang + '/?s=' + compound

    page = requests.get(url)

    soup = BeautifulSoup(page.text, "html.parser")

    information = soup.findAll('ul')

    for data in information:
        return data.text


    