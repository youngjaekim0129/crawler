import requests
from bs4 import BeautifulSoup
from datetime import datetime
import common

try:
    today = datetime.today().date()
    today = str(today.year)+'-'+str(today.month)+'-'+str(today.day)
    today = '2017-11-28'
    req = requests.get("http://www.ihalla.com/search_old.php?mode=Y&searchword=%EB%8F%99%EB%B6%80&search_type=0&s_category=T§ion=&s_day="+today+"&e_day="+today+"&x=139&y=12")
    html = req.text
    soup = BeautifulSoup(html,'html.parser')

    for link in soup.select('td.title > a'):
        session = requests.Session()
        session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
        req = session.get("http://www.ihalla.com"+link.get('href'))
        html = req.content
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.select('div.cont_gisa')
        common.count(body)
except Exception as e:
    print(e)