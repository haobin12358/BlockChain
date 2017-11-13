#coding = utf-8
from selenium import webdriver

class OpenBrowser():
    def open_browser(self, url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        try:
            driver.find_element_by_xpath('//*[@id="nav-user-account"]/div[1]/div/span[1]/a[1]').click()
        except:
            print 'fail to get //*[@id="nav-user-account"]/div[1]/div/span[1]/a[1]'

        try:
            pass
        except:
            print 'input error'

        print 'end'
if __name__ == '__main__':
    test = OpenBrowser()
    test.open_browser('https://ru.aliexpress.com')
