from selenium import webdriver
import time
import unittest

class test_class(unittest.TestCase):
    def test_reg1(self):
        self.link = "http://suninjuly.github.io/registration1.html"
        self.browser = webdriver.Chrome()
        self.browser.get(self.link)


        self.first=self.browser.find_element_by_css_selector('.form-group.first_class>input[placeholder="Input your first name"]')
        self.first.send_keys("Kolya")
        time.sleep(1)

        self.second = self.browser.find_element_by_css_selector('.form-group.second_class>input[placeholder="Input your last name"]')
        self.second.send_keys("Ladyn")
        time.sleep(1)

        self.third = self.browser.find_element_by_css_selector('.form-group.third_class>input[placeholder="Input your email"]')
        self.third.send_keys("try@try.ru")
        time.sleep(1)

        # Отправляем заполненную форму
        self.button = self.browser.find_element_by_css_selector("button.btn")
        self.button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
        time.sleep(1)

    # находим элемент, содержащий текст
        self.welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        print(type(self.welcome_text_elt))
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
        self.welcome_text = self.welcome_text_elt.text
        print(type(self.welcome_text))

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(self.welcome_text, "Congratulations! You have successfully registered!")
        self.browser.quit()
        print("GOOD")

    def test_reg2(self):

        self.link = "http://suninjuly.github.io/registration2.html"
        self.browser = webdriver.Chrome()
        self.browser.get(self.link)

            # Ваш код, который заполняет обязательные поля
        self.first = self.browser.find_element_by_css_selector('.form-group.first_class>input[placeholder="Input your name"]')
        self.first.send_keys("Kolya")
        time.sleep(1)

        self.second = self.browser.find_element_by_css_selector('.form-group.second_class>input[placeholder="Input your last name"]')
        self.second.send_keys("Ladyn")

        time.sleep(1)

        self.third = self.browser.find_element_by_css_selector('.form-group.third_class>input[placeholder="Input your email"]')
        self.third.send_keys("try@try.ru")
        time.sleep(1)

            # Отправляем заполненную форму
        self.button = self.browser.find_element_by_css_selector("button.btn")
        self.button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
        time.sleep(1)

            # находим элемент, содержащий текст
        self.welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        print(type(self.welcome_text_elt))
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
        self.welcome_text = self.welcome_text_elt.text
        print(type(self.welcome_text))

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(self.welcome_text, "Congratulations! You have successfully registered!")
        self.browser.quit()
        print("GOOD")

if __name__ == "__main__":
    unittest.main()
