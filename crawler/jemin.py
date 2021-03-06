import requests
from bs4 import BeautifulSoup
from datetime import datetime
import common

try:
    today = datetime.today().date()
    today = str(today.year)+'-'+str(today.month)+'-'+str(today.day)
    req = requests.get("http://www.jemin.com/engine_yonhap/search.php?picktab=article&searchcont=article&div_code=&others_cont_type=&page=1&sort=&searchword=%B5%BF%BA%CE&period=1m&from_date="+today+"&to_date="+today+"&cust_div_code=&sfield=&article_type=")
    html = req.text
    soup = BeautifulSoup(html,'html.parser')

    for link in soup.select('div.txtbox > strong > a'):
        session = requests.Session()
        session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
        req = session.get(link.get('href'))
        html = req.content
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.select('#articleBody')
        common.count(body)
except Exception as e:
    print(e)