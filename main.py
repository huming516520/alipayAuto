import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait                            # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC

from alipay import alipay

if __name__ == '__main__':
    zfb = alipay()
    zfb.manyTransfer([])
    print("main start")