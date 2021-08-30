from selenium import webdriver
import time
from math import sin, log, e

link="http://suninjuly.github.io/redirect_accept.html"

driver = webdriver.Chrome()
driver.get(link)

button = driver.find_element_by_class_name("btn")
button.click()

alert = driver.switch_to.alert
alert.accept()

x = int(driver.find_element_by_id("input_value").text)
print(x)
y = str(log(abs(12*sin(x)), e))

answer=driver.find_element_by_id("answer")
answer.send_keys(y)

button = driver.find_element_by_class_name("btn")
button.click()