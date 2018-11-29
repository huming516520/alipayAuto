
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait                            # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC


class alipay:
    def __init__(self):
        self.web = webdriver.Chrome( 'chromedriver')
        self.web.get('https://shenghuo.alipay.com/transfer/otmpay/fill.htm')
    def __del__(self):
        self.web.quit()

    def waitElements(self, name, by=By.CLASS_NAME, time=10):
        try:
            wait = WebDriverWait( self.web, time )
            wait.until( EC.visibility_of_element_located( (by, name) ) )
            return True
        except:
            return False

    def addPointer(self):
        try:
            self.waitElements( name='add-pointer', time=3000 )
            self.web.find_element_by_class_name( 'add-pointer' ).click()  # 增加收款人
            return True
        except:
            return  False

    def fillManyTransfer(self, accounts, index):
        if index >= 20:
            return
        if index > 0:
            index = index + 1
        print('fillManyTransfer', accounts, index, len(self.web.find_elements_by_class_name( 'ui-form-item2' )))
        try:
            if self.waitElements( name='ui-form-item2', time=3000 ):
                elements = self.web.find_elements_by_class_name( 'ui-form-item2' )
                #if (index + 5) >= len(elements):    #人不够，增加
                self.addPointer()
                element = self.web.find_elements_by_class_name( 'ui-form-item2' )[index]
                element.find_element_by_class_name( 'account-display' ).click()
                element.find_element_by_class_name( 'account-display' ).send_keys( accounts[1] )
                element.find_element_by_class_name( 'amount' ).click()
                element.find_element_by_class_name( 'amount' ).send_keys( str(accounts[2]) )
                element.find_element_by_class_name( 'account-display' ).click()
                time.sleep( 1 )
                element.find_element_by_class_name( 'amount' ).click()

                try:
                    if self.waitElements(name='account-error', time=1):
                        element.find_element_by_class_name( 'ico-del' ).click()
                        time.sleep( 1 )
                        #element.find_element_by_class_name( 'amount' ).clear()
                        return False
                    else:
                        print( 'fillManyTransfer Success' )
                        return True
                except Exception as e:
                    print('fillManyTransfer Success')
                    print(e)
                    return True
            else:
                return False
        except Exception as e:
            print(e)
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



