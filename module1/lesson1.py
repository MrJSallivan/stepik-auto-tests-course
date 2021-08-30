from selenium import webdriver
import time
import math

browser=webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_link_text")
time.sleep(5)

link=str(math.ceil(math.pow(math.pi, math.e)*10000))

find=browser.find_element_by_link_text("{0}".format(link))
time.sleep(5)
find.click()

input1 = browser.find_element_by_tag_name("div.form-group:nth-child(1)>input")
input1.send_keys("Ivan")
input2 = browser.find_element_by_name("last_name")
input2.send_keys("Petrov")
input3 = browser.find_element_by_class_name("form-group:nth-child(3)>.form-control")
input3.send_keys("Smolensk")
input4 = browser.find_element_by_id('country')
input4.send_keys("Russia")
button = browser.find_element_by_css_selector("button.btn")
button.click()

