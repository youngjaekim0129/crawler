import requests
from bs4 import BeautifulSoup
from datetime import datetime
import common

try:
    today = datetime.today().date()
    today = str(today.year)+'-'+str(today.month)+'-'+str(today.day)
    req = requests.get("http://search.hankyung.com/apps.frm/search.news?query=%EB%8F%99%EB%B6%80&sort=DATE%2FDESC%2CRANK%2FDESC&period=DAY&area=ALL&mediaid_clust=HKPAPER&exact=&include=&except=")
    html = req.text
    soup = BeautifulSoup(html,'html.parser')

    for link in soup.select('div.section.hk_news > div > ul > li > div > a'):
        session = requests.Session()
        session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
        req = session.get(link.get('href'))
        html = req.content
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.select('#newsView')
        common.count(body)
except Exception as e:
    print(e)