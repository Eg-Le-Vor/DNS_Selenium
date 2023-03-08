import time
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"""Локаторы"""

SMARTPHONE_NAME_LOCATOR = "/html/body/div/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[1]/div[1]/div[3]/div/div[1]/a"
SMARTPHONE_PRICE_LOCATOR = "/html/body/div/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[1]/div[3]/div/div[1]/div[1]/span[2]"


class Cart_page(Base):

    def __init__(self, driver, check_name, check_price):
        super().__init__(driver)
        self.driver = driver
        self.check_name = check_name
        self.check_price = check_price
    

    """Геттеры"""

    def get_smartphone_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, SMARTPHONE_NAME_LOCATOR)))

    def get_smartphone_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, SMARTPHONE_PRICE_LOCATOR)))


    """Действия"""

    def check_smartphone_name(self):
        assert self.check_name in self.get_smartphone_name().text.replace(' ', '')
        print('Название верное.')
    
    def check_smartphone_price(self):
        assert self.check_price in self.get_smartphone_price().text.replace(' ', '')
        print('Цена верная.')


    """Методы"""

    def finish(self):
        self.check_u = "https://www.dns-shop.ru/cart/"

        self.get_current_url()
        self.check_url(self.check_u)
        self.check_smartphone_name()
        self.check_smartphone_price()
        self.get_screenshot()