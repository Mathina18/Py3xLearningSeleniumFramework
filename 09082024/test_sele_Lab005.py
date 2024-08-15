import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_open_vwologin():
    #chrome_options = Options()
    #chrome_options.add_extension("C:/Users/LENOVO/Downloads/AdBlocker.crx")
    driver = webdriver.Chrome()
    driver.get("https://youtube.com")
    driver.maximize_window()
    time.sleep(10)
