# 시아 크롤링
import urllib.request
from bs4 import BeautifulSoup

#URL만 수정하면 됨
url="https://kr.iherb.com/c/vitamin-b"

#403 에러 방지를 위한 User-Agent 설정
hdr = {'User-Agent' :'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
req=urllib.request.Request(url=url, headers=hdr)
response = urllib.request.urlopen(req)
soup = BeautifulSoup(response, "html.parser")

values = soup.find_all(class_='product-title')
for value in values:
    print (value.text.strip())

#Rating의 경우 보강 필요.
ratings = soup.find(class_='rating-count')['title']
for rating in ratings:
    print(rating)

prices = soup.find_all(class_='price')
for price in prices:
    print(price.text.strip())
