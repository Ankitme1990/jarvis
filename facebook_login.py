from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# def auto_log():
#     def account_info():
#         with open('account_info.txt', 'r') as f:
#             info = f.read().split()
#             email = info[0]
#             password = info[1]
#             print(email)
#         return email, password
#
#     ser = Service("chromedriver.exe")
#     email, password = account_info()
#     chrome_options = Options()
#     chrome_options.add_experimental_option("detach", True)
#     chrome_options.add_argument("start-maximized")
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.get('https://www.facebook.com/')
#     time.sleep(2)
#     driver.find_element('id', 'email').send_keys(email)
#
#     time.sleep(3)
#     driver.find_element('id', 'pass').send_keys(password)
#
#     time.sleep(3)
#     driver.find_element('name', 'login').click()


def auto_log():
    def account_info():
        with open('account_info.txt', 'r') as f:
            info = f.read().split()
            email = info[0]
            password = info[1]
            print(email)
        return email, password

    ser = Service("chromedriver.exe")
    email, password = account_info()
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.facebook.com/')
    time.sleep(2)
    driver.find_element('id', 'email').send_keys(email)

    time.sleep(3)
    driver.find_element('id', 'pass').send_keys(password)

    time.sleep(3)
    driver.find_element('name', 'login').click()

    time.sleep(5)  # Wait for page to load and notification pop-up to appear
    try:
        driver.switch_to.alert.accept()  # Accept the browser alert dialog, which should be the notification pop-up
    except:
        pass  # If no notification pop-up appears or cannot be clicked, continue with the script


# auto_log()
