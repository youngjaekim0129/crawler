import requests
from bs4 import BeautifulSoup
from datetime import datetime
import common

try:
    today = datetime.today().date()
    today = str(today.year)+'-'+str(today.month)+'-'+str(today.day)
    req = requests.get("http://www.ccdailynews.com/engine_yonhap/search.php?div_code=&cust_div_code=&sfield=&article_type=&others_cont_type=&period=0d&from_date="+today+"&to_date="+today+"&searchword=%B5%BF%BA%CE&picktab=article")
    html = req.text
    soup = BeautifulSoup(html,'html.parser')

    for link in soup.select('div > strong > a'):
        session = requests.Session()
        session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
        req = session.get(link.get('href'))
        html = req.content
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.select('#articleBody')
        common.count(body)
except Exception as e:
    print(e)