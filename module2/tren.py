from selenium import webdriver
from math import sin, log, e
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд


browser.get("http://suninjuly.github.io/explicit_wait2.html")
time.sleep(1)
price = browser.find_element_by_id("price").text
price=price[1:]
print(price)
