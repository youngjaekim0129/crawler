import requests
from bs4 import BeautifulSoup
from datetime import datetime
import common

try:
    today = datetime.today().date()
    today = str(today.year)+'.'+str(today.month)+'.'+str(today.day)
    req = requests.get("http://search.chosun.com/search/news.search?query=%EB%8F%99%EB%B6%80&pageno=0&orderby=news&naviarraystr=&kind=&cont1=&cont2=&cont5=&categoryname=%EC%A1%B0%EC%84%A0%EC%9D%BC%EB%B3%B4&categoryd2=&c_scope=navi&sdate="+today+"&edate="+today+"&premium=")
    html = req.text
    soup = BeautifulSoup(html,'html.parser')

    for link in soup.select('dt > a'):
        session = requests.Session()
        session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
        req = session.get(link.get('href'))
        html = req.content.decode('euc-kr')
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.select('#news_body_id > div.par')
        common.count(body)
except Exception as e:
    print(e)