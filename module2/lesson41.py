from selenium import webdriver
from math import sin, log, e
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд


browser.get("http://suninjuly.github.io/explicit_wait2.html")

def getprice():
    time.sleep(1)
    price=99999
    while price>100:
        price= browser.find_element_by_id("price").text
        price=int(price[1:])
    return price


price= WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID,"price"),"{0}".format(getprice())))
button=browser.find_element_by_id("book")
button.click()



x = int(browser.find_element_by_id("input_value").text)
print(x)
y = str(log(abs(12*sin(x)), e))


answer=browser.find_element_by_id("answer")
answer.send_keys(y)


button = browser.find_element_by_id("solve")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()