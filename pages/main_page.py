import time
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Main_page(Base):

    product_name = "лопата"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    # локаторы записываем в переменные
    input_product = "//input[@id='title-search-input']"
    serch_button = "//button[@class='btn white search-btn']"


    #Getters
    # находим элементы по локатору
    def get_input_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_product)))

    def get_click_for_search_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.serch_button)))


    #Actions
    # что-то вводим или нажимаем кнопки
    def input_name_product(self, product_name):
        self.get_input_product().send_keys(product_name)
        print("Ввели название товара")

    def click_serch_button(self):
        self.get_click_for_search_product().click()
        print("Нажали на кнопку поиска товара")
        # time.sleep(5)


    #Methods
    # вызываем к выполнению
    def input_product_for_search(self):
        self.get_current_url()
        self.input_name_product(self.product_name)
        self.click_serch_button()








