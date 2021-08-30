from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first=browser.find_element_by_css_selector('.form-group.first_class>input[placeholder="Input your first name"]')
    first.send_keys("Kolya")
    time.sleep(1)

    second = browser.find_element_by_css_selector('.form-group.second_class>input[placeholder="Input your last name"]')
    second.send_keys("Ladyn")
    time.sleep(1)

    first = browser.find_element_by_css_selector('.form-group.third_class>input[placeholder="Input your email"]')
    first.send_keys("try@try.ru")
    time.sleep(1)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    print(type(welcome_text_elt))
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    print(type(welcome_text))

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()