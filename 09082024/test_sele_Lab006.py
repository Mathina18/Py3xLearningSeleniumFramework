import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    driver.refresh()
    driver.back()
    driver.forward()
    #print(driver.page_source)
    # driver.close()
    # time.sleep(10) #use sleep after close to close the current tab
    #close will close the current window or tab
    # session_id != null(Invalid)
    #it will not close the other tabs
    time.sleep(10)
    driver.quit()