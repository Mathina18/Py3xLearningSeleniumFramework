import time

from selenium import webdriver

def test_open_vwologin():
    driver = webdriver.Chrome() #b5ff62a0434221dd6ade4843d6a7919a
    # Code -> HTTP rEQUEST - POST
    # POST request | Create the Session
    # Session is created - Unique ID - 16 digit ID
    # driver = webdriver.Edge() #4d4cd0cf86c201a2b0120245892406a2
    # driver = webdriver.Firefox()
    # Code -> HTTP rEQWUST -. cHROMEdRIVE -> chROME (SessionID)
    print(driver.session_id)
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert driver.title == "Login - VWO"
    time.sleep(10)  # Python Int - to stop for the 10 seconds