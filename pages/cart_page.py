import time

from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Cart_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    # локаторы записываем в переменные
    button_place_an_order = "//button[@class='btn btn-lg btn-default basket-btn-checkout white']"


    #Getters
    # находим элементы по локатору
    def get_button_place_an_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_place_an_order)))


    #Actions
    # что-то вводим или нажимаем кнопки
    def click_button_place_an_order(self):
        self.get_button_place_an_order().click()
        print("Нажали кнопку 'Оформить заказ'")
        # time.sleep(3)


    #Methods
    # вызываем к выполнению
    def use_cart_page(self):
        self.get_current_url() #получаем URL
        self.click_button_place_an_order() #нажимаем на кнопку "Оформить заказ"















