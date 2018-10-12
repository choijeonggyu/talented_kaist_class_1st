## parser.py
import requests
from bs4 import BeautifulSoup


## HTTP GET Request
req = requests.get('https://beomi.github.io/beomi.github.io_old/')

##HTML 소스 가져오기
html = req.text

soup = BeautifulSoup(html, 'html.parser')
## CSS Selector를 통해서 HTML 요소들을 찾아낸다.
my_titles = soup.select(
    'h3 > a'
)

##my_titles 는 list 객체
for title in my_titles:
    ##Tag 안의 텍스트
    print(title.text)
    ##Tag 의 속성을 가져오기(ex: href 속성)
    print(title.get('href'))

