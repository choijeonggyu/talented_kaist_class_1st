import requests
from bs4 import BeautifulSoup as bs

LOGIN_INFO= {
    'userId' : 'willy222', 'userPassword': 'brave222'
}
#Session  생성, with 구문안에서 유지
with requests.Session() as s:
    #우선 클리앙 홈페이지에 들어가 봅시다.
    first_page = s.get('https://www.clien.net/service')
    html = first_page.text
    soup = bs(html, 'html.parser')
    csrf = soup.find('input',{'name': '_csrf'})  #input 태그 중에서 name 이 _csrf 인 것을 찾습니다.
    print(csrf['value'])

    #이제 LOGIN_INFO 에 csrf 값을 넣어줍시다.
    #(p.s) python3 에서 두 dict를 합치는 방법은 {**dict1, ** dict2}으로  dict 들을 unpacking 하는 것입니다.
    LOGIN_INFO = {**LOGIN_INFO, **{'_csrf': csrf['value']}}
    print(LOGIN_INFO)


    #이제 다시 로그인 해봅시다.
    login_req = s.post('https://www.clien.net/service/login',data = LOGIN_INFO)

    print(login_req.status_code)