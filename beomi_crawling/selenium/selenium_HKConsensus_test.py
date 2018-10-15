from selenium import webdriver
import time


def get_download(links):
    download_dir = "C:\\Temp\\stockMarketReportPDF"  # for linux/*nix, download_dir="/usr/Public"
    options = webdriver.ChromeOptions()

    profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],  # Disable Chrome's PDF Viewer
               "download.default_directory": download_dir, "download.extensions_to_open": "applications/pdf"}
    options.add_experimental_option("prefs", profile)
    driver = webdriver.Chrome('C:\\driver\\chromedriver.exe',
                              chrome_options=options)  # Optional argument, if not specified will search path.

    driver.get(links)


# 크롬의 경우 chrome driver의 위치를 지정해 준다.
driver = webdriver.Chrome('c:\driver\chromedriver.exe')
## PhantomJS의  경우도 마찬가지
# driver = webdriver.PhantomJS('C:\driver\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.implicitly_wait(5)
##URL에 접근한다.,

driver.get('http://hkconsensus.hankyung.com/apps.analysis/analysis.list')

elements = driver.find_elements_by_xpath('//*[@id="contents"]/div/table/tbody/tr/td/div/a')
links = []

for i in range(len(elements)):
    links.append(elements[i].get_attribute('href'))

for link in links:
    print('navigating to: ' + link)
    get_download(link)

    time.sleep(1)

"""
    driver.get(link)

    # do stuff within that page here...

    driver.back()
"""

