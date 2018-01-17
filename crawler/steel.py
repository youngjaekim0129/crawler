import requests
from bs4 import BeautifulSoup
from datetime import datetime
import common
import time

def crawl():
    try:
        customer_list = common.get_customer_list()
        for customer in customer_list:
            today = datetime.today().date()
            today = str(today.year)+'-'+str(today.month)+'-'+str(today.day)
            proxies = {'http':'http://172.30.4.18:8080'}
            req = requests.get("http://steel.today.kr/ct_list.php?stxt="+customer[0], proxies=proxies)
            html = req.text
            soup = BeautifulSoup(html,'html.parser')

            for link in soup.select('span > h3 > a'):
                session = requests.Session()
                session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
                req = session.get("http://steel.today.kr/"+link.get('href'), proxies=proxies)
                html = req.content
                soup = BeautifulSoup(html, 'html.parser')
                body = soup.select('span.Reporter_time > p')
                if body[2].get_text().find(today) != -1:
                    body = soup.select('span.news_view_text')
                    common.count(body,customer,'철강신문',"http://steel.today.kr/"+link.get('href'))
            time.sleep(0.5)
    except Exception as e:
        print(e)