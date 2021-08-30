import os
from selenium import webdriver
import time

driver = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
driver.get(link)

firstname=driver.find_element_by_name("firstname")
firstname.send_keys("ПРивет")

firstname=driver.find_element_by_name("lastname")
firstname.send_keys("Пока")

firstname=driver.find_element_by_name("email")
firstname.send_keys("ПРивет@пока.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
file = driver.find_element_by_css_selector("input#file")

file.send_keys(file_path)

button = driver.find_element_by_css_selector(".btn")
button.click()

