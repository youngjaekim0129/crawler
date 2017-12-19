import requests
from bs4 import BeautifulSoup
from datetime import datetime
import common

try:
    today = datetime.today().date()
    today = str(today.year)+'-'+str(today.month)+'-'+str(today.day)
    req = requests.get("http://www.idomin.com/?mod=search&act=engine&sc_code=&sc_sdate="+today+"&sc_edate="+today+"&sc_word=%EB%8F%99%EB%B6%80&sc_andor=OR&sc_word2=")
    html = req.text
    soup = BeautifulSoup(html,'html.parser')

    i = 1
    for link in soup.select('td > a'):
        if i % 2 == 1:
            session = requests.Session()
            session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
            req = session.get("http://www.idomin.com"+link.get('href'))
            html = req.content
            soup = BeautifulSoup(html, 'html.parser')
            body = soup.select('#arl_view_box')
            common.count(body)
        i = i + 1
except Exception as e:
    print(e)