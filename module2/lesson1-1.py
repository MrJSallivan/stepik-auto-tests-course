from selenium import webdriver
import time
from math import sin, log, e

link="http://suninjuly.github.io/math.html"

driver = webdriver.Chrome()
driver.get(link)

value = driver.find_element_by_id("input_value")
x = int(value.text)
print(x)
y = str(log(abs(12*sin(x)),e))


field = driver.find_element_by_class_name("form-control")
field.send_keys(y)



select1 = driver.find_element_by_css_selector("[for='robotCheckbox']")
select1.click()


select2 = driver.find_element_by_css_selector("[for='robotsRule']")
select2.click()


button = driver.find_element_by_css_selector(".btn")
button.click()






