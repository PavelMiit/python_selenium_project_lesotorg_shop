import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Filter_page(Base):

    price_min = "99"
    price_max = "6000"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.action = ActionChains(driver)

    #Locators
    # локаторы записываем в переменныее
    filter_price_min = "//input[@id='property_P_min']"
    filter_price_max = "//input[@id='property_P_max']"
    filter_width_left_slider = "//*[@id='left_slider_829']"
    product_tab = "//a[@id='bx_2738408476_98336_pict']"




    #Getters
    # находим элементы по локатору
    def get_filter_price_min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_price_min)))

    def get_filter_price_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_price_max)))

    def get_filter_width_left_slider(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_width_left_slider)))

    def get_product_tab(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_tab)))





    #Actions
    # что-то вводим или нажимаем кнопкииeeee
    def input_filter_price_min(self, price_min):
        self.get_filter_price_min().send_keys(price_min)
        print("Ввели минимальную стоимость товара: "+ price_min)

    def input_filter_price_max(self, price_max):
        self.get_filter_price_max().send_keys(price_max)
        print("Ввели максимальную стоимость товара: "+ price_max)
        time.sleep(3)

    def move_filter_width_left_slider(self):
        self.driver.execute_script("window.scrollTo(0, 600);") #скролл страницы на 6 см вниз, чтобы найти кнопку на слайдере
        self.action.click_and_hold(self.get_filter_width_left_slider()).pause(2).move_by_offset(25, 0).release().perform()
        self.driver.execute_script("window.scrollTo(0, 0);") #скролл страницы в самый верх
        print("Передвинули левый слайдер ширины")
        time.sleep(3)


    def click_product_tab(self):
        self.get_product_tab().click()
        print("Выбрали товар на странице фильтра")
        # time.sleep(3)


    #Methods
    # вызываем к выполнению
    def use_filter_page(self):
        self.get_current_url()
        self.input_filter_price_min(self.price_min)
        self.input_filter_price_max(self.price_max)
        self.move_filter_width_left_slider()
        self.click_product_tab()











