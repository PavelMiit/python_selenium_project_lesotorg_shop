import datetime

class Base():

    def __init__(self, driver):
        self.driver = driver


    """Method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("URL страницы: " + get_url)


    """Method assert word"""
    def assert_word(self, word, result_world):
        value_word = word.text
        assert value_word == result_world
        print("Успешно проверили название товара: " + value_word)


    """Method assert price"""
    def assert_price(self, price, result_price):
        value_price = price.text
        assert value_price == result_price
        print("Успешно проверили стоимость товара: " + value_price)


    """Method Screenshot"""
    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%H.%M.%S-%Y.%m.%d")
        name_screenshot = "screenshot " + now_date + ".png"
        self.driver.save_screenshot('C:\\Users\\pmitc\\pythonLesson\\selenium_project_lesotorg_shop\\screen\\' + name_screenshot)
        print("Сделали скриншот: " + name_screenshot)


    """Method assert url"""
    def assert_url(self, result_url):
        get_url = self.driver.current_url
        assert get_url == result_url
        print("Успешно сравнили URL")

