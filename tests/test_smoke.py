from selenium import webdriver
from pages.authorization_page import Authorization_page
from pages.cart_page import Cart_page
from pages.filter_page import Filter_page
from pages.main_page import Main_page
from pages.product_page import Product_page


def test_smoke_product():
    driver = webdriver.Chrome()
    base_url = 'https://leso-torg.ru/'
    driver.get(base_url)
    driver.maximize_window()

    print("Старт теста")

    search_product = Main_page(driver) #создали объект экземпляра класса Main_page
    search_product.input_product_for_search() #обратились к экземлпяру класса search_product и вызвали метод ввода названия товара в строку поиска и клика по кнопке "Поиск"

    filter_page = Filter_page(driver)
    filter_page.use_filter_page() #вызвали метод работы с фильтрами на странице filter page

    product_page = Product_page(driver)
    product_page.use_product_page() #вызвали метод сравнения названия товара и его цены на странице product page и добавления товара в корзину

    cart_page = Cart_page(driver)
    cart_page.use_cart_page() #вызвали метод нажатия кнопки "Оформить заказ"на странице cart page

    authorization_page = Authorization_page(driver)
    authorization_page.use_authorization_page() #вызвали метод заполнения полей, получения скриншота и сравнения URL на странице authorization page









