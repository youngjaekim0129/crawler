import requests
from bs4 import BeautifulSoup
from konlpy.tag import Mecab
from datetime import datetime

try:
    today = datetime.today().date()
    today = str(today.year)+'-'+str(today.month)+'-'+str(today.day)
    today = '2017-12-07'
    req = requests.get("http://www.inews365.com/news/search_result.html?search_mode=multi&s_title=1&search=%EB%8F%99%EB%B6%80&s_sdate="+today+"&s_edate="+today+"&catno=")
    html = req.text
    soup = BeautifulSoup(html,'html.parser')
    mecab = Mecab()

    for link in soup.select('#alt1 > ul > li > a'):
        session = requests.Session()
        session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
        req = session.get(link.get('href'))
        html = req.content
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.select('#news_body_area')
        if len(body) != 0 :
            text = body[0].get_text()

            f = open("keyword.txt",'r')
            while True:
                line = f.readline()
                line = line.replace('\n','')
                if not line: break
                text = text.replace(line,'부실')
            f.close()

            nouns = mecab.nouns(text)
            print(nouns.count('부실'))
except Exception as e:
    print(e)