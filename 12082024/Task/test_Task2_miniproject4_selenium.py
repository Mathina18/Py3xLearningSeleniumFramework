import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@pytest.mark.positive
@allure.title("Verify the URL changes in cuba health care website - test_mini_project_3")
@allure.description("Verify that user able to make appointment button and login to check the make appointment header")
def test_task_mini_project_4():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    makeappointment_button_element = driver.find_element(By.ID, "btn-make-appointment")
    makeappointment_button_element.click()

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(5)

    username_web_element = driver.find_element(By.ID, "txt-username")
    username_web_element.send_keys("John Doe")

    password_web_element = driver.find_element(By.ID, "txt-password")
    password_web_element.send_keys("ThisIsNotAPassword")

    login_button_element = driver.find_element(By.ID, "btn-login")
    login_button_element.click()

    make_appointment = driver.find_element(By.TAG_NAME, "h2")
    assert make_appointment.text == "Make Appointment"

    # For allure screenshot
    allure.attach(driver.get_screenshot_as_png(), name='appointment_screenshot')
    time.sleep(3)
    driver.quit()