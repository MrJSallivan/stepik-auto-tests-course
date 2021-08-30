from selenium import webdriver
import time
from math import sin, log, e

link = "http://suninjuly.github.io/get_attribute.html"

driver = webdriver.Chrome()
driver.get(link)

value = driver.find_element_by_tag_name("img")
x = int(value.get_attribute("valuex"))
print(x)
y = str(log(abs(12*sin(x)), e))


field = driver.find_element_by_id("answer")
field.send_keys(y)



select1 = driver.find_element_by_id("robotCheckbox")
select1.click()


select2 = driver.find_element_by_css_selector("#robotsRule")
select2.click()


button = driver.find_element_by_css_selector(".btn")
button.click()
