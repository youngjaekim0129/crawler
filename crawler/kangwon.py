import requests
from bs4 import BeautifulSoup
from datetime import datetime
import common

try:
    today = datetime.today().date()
    today = str(today.year)+'-'+str(today.month)+'-'+str(today.day)
    req = requests.get("http://www.kado.net/?mod=search&act=engine&cust_div_code=&searchContType=article&searchWord=%EB%8F%99%EB%B6%80&period=0d&fromDate="+today+"&toDate="+today)
    html = req.text
    soup = BeautifulSoup(html,'html.parser')

    for link in soup.select('li.li.ellipsis.title > a'):
        session = requests.Session()
        session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
        req = session.get(link.get('href'))
        html = req.content
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.select('#arl_view_content')
        common.count(body)
except Exception as e:
    print(e)