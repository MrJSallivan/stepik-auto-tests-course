import time
from selenium import webdriver

driver = webdriver.Chrome()
time.sleep(5)

driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

submit_button = driver.find_element_by_css_selector(".st-link_style_button")
submit_button.click()
time.sleep(5)

login = driver.find_element_by_css_selector(".sign-form__input")
login.send_keys("vasyapoposkin@yandex.ru")
time.sleep(5)

password = driver.find_element_by_xpath("//*[contains(@id,'password')]")
password.send_keys("nhfdjknf")
time.sleep(5)

submit_button = driver.find_element_by_css_selector(".button_with-loader")
submit_button.click()

textarea = driver.find_element_by_css_selector(".textarea")
textarea.send_keys("get()")
time.sleep(5)

submit_button = driver.find_element_by_css_selector(".submit-submission")
submit_button.click()
time.sleep(5)

driver.quit()