from selenium import webdriver
import time
from math import sin, log, e
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
driver.get(link)

x = int(driver.find_element_by_id("input_value").text)
print(x)
y = str(log(abs(12*sin(x)), e))

field = driver.find_element_by_class_name("form-control")
field.send_keys(y)


checkbox = driver.find_element_by_css_selector("[for='robotCheckbox']")
checkbox.click()


radio = driver.find_element_by_css_selector("[for='robotsRule']")
driver.execute_script("window.scrollBy(0, 100);")

radio.click()


button = driver.find_element_by_css_selector(".btn")
button.click()


time.sleep(5)



