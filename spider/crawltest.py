from urllib2 import urlopen,Request
from bs4 import BeautifulSoup
import threading
from time import ctime,sleep
import random
import requests
import re
header={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Connection': 'keep-alive',
            'Host': 'apps.webofknowledge.com',
            'Upgrade-Insecure-Requests': '1',
        }
url = 'http://apps.webofknowledge.com/summary.do?locale=en_US&errorKey=&viewType=summary&mode=refine&product=WOS&search_mode=GeneralSearch&colName=WOS&parentQid=1&qid=2&SID=Q2quEMGbgLdzhxfjZh3'
req = Request(url, None, header)
response = urlopen(req,timeout=5)
bibliographypage = response.read()

html = BeautifulSoup(bibliographypage,'html.parser')
print (html.find_all(text=re.compile('Highly Cited Paper')))
print (html.find_all(text=re.compile('Hot Paper')))





