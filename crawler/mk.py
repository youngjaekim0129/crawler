import requests
from bs4 import BeautifulSoup
from datetime import datetime
import common

try:
    today = datetime.today().date()
    year = str(today.year)
    month = str(today.month)
    day = str(today.day)
    req = requests.get("http://find.mk.co.kr/new/search.php?pageNum=1&cat=00001&cat1=&media_eco=&pageSize=10&sub=all&dispFlag=OFF&page=total&s_kwd=%B5%BF%BA%CE&s_page=total&go_page=&ord=1&ord1=1&ord2=0&s_keyword=%B5%BF%BA%CE&y1="+year+"&m1="+month+"&d1="+day+"&y2="+year+"&m2="+month+"&d2="+day+"&area=ttbd")
    html = req.text
    soup = BeautifulSoup(html,'html.parser')

    for link in soup.select('span.art_tit > a'):
        session = requests.Session()
        session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
        req = session.get(link.get('href'))
        html = req.content
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.select('#article_body')
        common.count(body)
except Exception as e:
    print(e)