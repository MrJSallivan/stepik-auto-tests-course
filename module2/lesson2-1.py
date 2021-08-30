from selenium import webdriver
import time
from math import sin, log, e
from selenium.webdriver.support.ui import Select


link="http://suninjuly.github.io/selects1.html"

driver = webdriver.Chrome()
driver.get(link)

num1 = int(driver.find_element_by_id("num1").text)
print(num1)
num2 = int(driver.find_element_by_id("num2").text)
print(num2)
summa = num1+num2
print(summa)

dropdown = Select(driver.find_element_by_tag_name("select"))
dropdown.select_by_value("{0}".format(summa))

button = driver.find_element_by_css_selector(".btn")
button.click()
