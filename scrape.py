from bs4 import BeautifulSoup
import requests
from csv import writer

url="https://stock.wearn.com/a50m.asp"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('table')
#print (lists[0])
for list in lists:
    alltabletd1 = list.find_all('tr', class_='stockalllistbg1')
    alltabletd2 = list.find_all('tr', class_='stockalllistbg2')

    for tabletd in alltabletd2: 
        code = tabletd.find_all('td')[1].get_text()
        buy = tabletd.find_all('td')[3].get_text()
        sell = tabletd.find_all('td')[4].get_text()
        amt = tabletd.find_all('td')[5].get_text()
        print(code, buy, sell, amt)

    for tabletd in alltabletd1: 
        code = tabletd.find_all('td')[1].get_text()
        buy = tabletd.find_all('td')[3].get_text()
        sell = tabletd.find_all('td')[4].get_text()
        amt = tabletd.find_all('td')[5].get_text()
        print(code, buy, sell, amt)
