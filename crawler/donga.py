import requests
from bs4 import BeautifulSoup
from datetime import datetime
import common

try:
    today = datetime.today().date()
    today = str(today.year)+str(today.month)+str(today.day)
    req = requests.get("http://news.donga.com/search?check_news=&more=&sorting=&range=&search_date=&search_date=5&v1="+today+"&v2="+today+"&query=%EB%8F%99%EB%B6%80")
    html = req.text
    soup = BeautifulSoup(html,'html.parser')

    for link in soup.select('p.tit > a'):
        session = requests.Session()
        session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
        req = session.get(link.get('href'))
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.select('div.article_txt')
        common.count(body)
except Exception as e:
    print(e)