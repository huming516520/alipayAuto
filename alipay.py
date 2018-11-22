
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait                            # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC


class alipay:
    def __init__(self):
        self.web = webdriver.Chrome( 'chromedriver')
        #self.web.get('https://shenghuo.alipay.com/transfer/otmpay/fill.htm')
    def __del__(self):
        self.web.quit()

    def waitElements(self, name, by=By.CLASS_NAME, time=10):
        try:
            wait = WebDriverWait( self.web, time )
            wait.until( EC.visibility_of_element_located( (by, name) ) )
            return True
        except:
            return False

    def manyTransfer(self, accounts):
        self.web.get( 'https://shenghuo.alipay.com/transfer/otmpay/fill.htm' )
        self.waitElements(name='add-pointer',time=1000)
        print("开始转账")
        element = self.web.find_element_by_class_name( 'add-pointer' ) #增加收款人

        for i in range(0,17):
            print("点击增加收款人")
            element.click()

        tables = self.web.find_elements_by_class_name( 'ui-form-item2' )
        print(len(tables))
        try:
            for element in tables:
                element.find_element_by_class_name('account-display').send_keys("123")
                element.find_element_by_class_name('amount').send_keys(123)
        except Exception as e:
            print(e)

