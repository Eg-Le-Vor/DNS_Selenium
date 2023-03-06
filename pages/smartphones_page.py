import time
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


"""Локаторы"""

MIN_PRICE_FIELD_LOCATOR = "//input[@class='ui-input-small__input ui-input-small__input_list'][@placeholder='от 2 999']"
MAX_PRICE_FIELD_LOCATOR = "//input[@class='ui-input-small__input ui-input-small__input_list'][@placeholder='до 169 299']"
MIN_PRICE_1 = "5000"
MAX_PRICE_1 = "50000"


class Smartphones_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Геттеры"""

    def get_min_price_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, MIN_PRICE_FIELD_LOCATOR)))
    
    def get_max_price_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, MAX_PRICE_FIELD_LOCATOR)))


    """Действия"""

    def fill_min_price_field(self, data):
        action = ActionChains(self.driver)
        min_price_field = self.get_min_price_field()
        action.move_to_element(min_price_field).perform()
        min_price_field.send_keys(data)
        print('Поле минимальной стоимости заполнено.')
    
    def fill_max_price_field(self, data):
        action = ActionChains(self.driver)
        max_price_field = self.get_max_price_field()
        action.move_to_element(max_price_field).perform()
        max_price_field.send_keys(data)
        print('Поле максимальной стоимости заполнено.')


    """Методы"""

    def select_smartphone_1(self):
        self.check_u = "https://www.dns-shop.ru/catalog/17a8a01d16404e77/smartfony/"

        self.load_page()
        self.get_current_url()
        self.check_url(self.check_u)
        self.fill_min_price_field(MIN_PRICE_1)
        self.fill_max_price_field(MAX_PRICE_1)