from selenium import webdriver

#크롬의 경우 chrome driver의 위치를 지정해 준다.
driver = webdriver.Chrome('c:\driver\chromedriver.exe')
## PhantomJS의  경우도 마찬가지
#driver = webdriver.PhantomJS('C:\driver\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.implicitly_wait(5)
##URL에 접근한다.,
#driver.get('https://google.com')
driver.get('https://nid.naver.com/nidlogin.login')

driver.find_element_by_name('id').send_keys('willy222')
driver.find_element_by_name('pw').send_keys('nabrave222')
## 로그인 버튼을 눌러주자
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
