#parser.py

import requests

#Sexssion  생성, with 구문안에서 유지
with requests.Session() as s:
    #HTTP GET Request; requests 대신 s 객체를 사용한다.
    req = s.get('https://www.clien.net/service/')
    #HTML 소스 가져오기
    html = req.text
    # HTTP Header 가벼오기
    header = req.headers
    #HTTP Status 가져오기 (200:정상)
    status = req.status_code
    #HTTP 가 정상적으로 되었는지 (True/False)
    is_ok = req.ok
    print(is_ok)