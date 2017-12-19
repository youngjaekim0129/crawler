import requests
from bs4 import BeautifulSoup
import common

try:
    req = requests.get("http://search.joins.com/totalnews?StartSearchDate=&EndSearchDate=&Keyword=%EB%8F%99%EB%B6%80&SortType=New&SearchCategoryType=TotalNews&PeriodType=OneDay&ScopeType=All&ServiceCode=&SourceGroupType=Joongang&ReporterCode=&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&MatchKeyword=&IncludeKeyword=&ExcluedeKeyword=")
    html = req.text
    soup = BeautifulSoup(html,'html.parser')

    for link in soup.select('strong > a'):
        session = requests.Session()
        session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
        req = session.get(link.get('href'))
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.select('#article_body')
        common.count(body)
except Exception as e:
    print(e)