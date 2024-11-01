import time

from faker import Faker
fake = Faker("ru_Ru")
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Authorization_page(Base):

    value_tel_number = fake.numerify('+7 (9##) ###-##-##')
    value_password = fake.password()


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    # локаторы записываем в переменные
    tel_number = "//input[@id='phone0']"
    password = "//input[@id='pass']"
    show_password_button = "//input[@id='one']"
    login_button = "//span[@class='web web2 btn btn-default']"


    #Getters
    # находим элементы по локатору
    def get_tel_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tel_number)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_show_password_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.show_password_button)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))


    #Actions
    # что-то вводим или нажимаем кнопки

    def input_tel_number(self, user_tel):
        self.get_tel_number().send_keys(user_tel) #ввели телефон
        print("Ввели телефон " + user_tel)

    def input_password(self, user_password):
        self.get_password().send_keys(user_password) #ввели пароль
        print("Ввели пароль")

    def click_show_password_button(self):
        self.get_show_password_button().click()
        print("Нажали чек-бокс 'Показать пароль'")

    def click_login_button(self):
        self.get_login_button().click()
        print("Нажали кнопку 'Войти'")
        time.sleep(3)


    #Methods
    # вызываем к выполнению
    def use_authorization_page(self):
        self.get_current_url()
        self.input_tel_number(self.value_tel_number)
        self.input_password(self.value_password)
        self.click_show_password_button()
        self.click_login_button()
        self.get_screenshot()
        self.assert_url("https://leso-torg.ru/order/")















