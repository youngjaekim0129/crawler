import requests
from bs4 import BeautifulSoup
from datetime import datetime
import common

try:
    today = datetime.today().date()
    today = str(today.year)+'-'+str(today.month)+'-'+str(today.day)
    req = requests.get("http://www.kwangju.co.kr/search_result.php3?mode=Y&searchword=%B5%BF%BA%CE&x=18&y=15&s_category=TC&secion=&s_day="+today+"&e_day="+today+"&gigan=365")
    html = req.text
    soup = BeautifulSoup(html,'html.parser')

    for link in soup.select('td > a'):
        session = requests.Session()
        session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
        if link.get('href')[0:5] == '/read':
            req = session.get("http://www.kwangju.co.kr"+link.get('href'))
            html = req.content
            soup = BeautifulSoup(html, 'html.parser')
            body = soup.select('#joinskmbox')
            common.count(body)
except Exception as e:
    print(e)