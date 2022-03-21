from bs4 import BeautifulSoup
import requests
from csv import writer
import sys
import io
import pymysql.cursors
from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

holidays = ['2022-04-04','2022-04-05','2022-05-02','2022-06-03', '2022-09-09', '2022-10-10']

if today not in holidays:

    url="https://stock.wearn.com/b50.asp"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    lists = soup.find_all('table')

    conn = pymysql.connect(host='db-mysql-sgp1-66974-do-user-8278374-0.b.db.ondigitalocean.com',
        port=25060,
        user='pythonuser',
        password='oqpPIs9FvhoEAL6P',
        db='tw',
        charset='utf8mb4')
    #print (lists[0])
    for list in lists:
        alltabletd1 = list.find_all('tr', class_='stockalllistbg1')
        alltabletd2 = list.find_all('tr', class_='stockalllistbg2')
        
        for tabletd in alltabletd2: 
            code = tabletd.find_all('td')[1].get_text()
            name = tabletd.find('a').get_text()
            buy = tabletd.find_all('td')[3].get_text().replace(",","")
            sell = tabletd.find_all('td')[4].get_text().replace(",","")
            amt = tabletd.find_all('td')[5].get_text().replace(",","")
            buyint = int(buy)
            sellint = int(sell)
            amtint = int(amt)
            print(code, name, buyint, sellint, amtint)
            with conn:        
                conn.ping()
                with conn.cursor() as cursor:
                    sql = 'REPLACE INTO `tru`(`code`,`buy`,`sell`,`amt`,`date`) VALUES (%s, %s, %s, %s, %s)'
                    cursor.execute(sql,(code, buyint, sellint, amtint, today))
                    conn.commit()

        for tabletd in alltabletd1: 
            code = tabletd.find_all('td')[1].get_text()
            name = tabletd.find('a').get_text()
            buy = tabletd.find_all('td')[3].get_text().replace(",","")
            sell = tabletd.find_all('td')[4].get_text().replace(",","")
            amt = tabletd.find_all('td')[5].get_text().replace(",","")
            print(code, name, buy, sell, amt)
            buyint = int(buy)
            sellint = int(sell)
            amtint = int(amt)
            print(code, name, buyint, sellint, amtint)
            with conn:        
                conn.ping()
                with conn.cursor() as cursor:
                    sql = 'REPLACE INTO `tru`(`code`,`buy`,`sell`,`amt`,`date`) VALUES (%s, %s, %s, %s, %s)'
                    cursor.execute(sql,(code, buyint, sellint, amtint, today))
                    conn.commit()
