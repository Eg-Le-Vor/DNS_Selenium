from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import Logger


"""Локаторы"""

SMARTPHONES_BUTTON_LOCATOR = "//a[@href='/catalog/17a8a01d16404e77/smartfony/'][@class='subcategory__item ui-link ui-link_blue']"


class Smartphones_gadgets_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Геттеры"""

    def get_smartphones_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, SMARTPHONES_BUTTON_LOCATOR)))


    """Действия"""

    def click_smartphones_button(self):
        self.get_smartphones_button().click()
        print('Нажата кнопка "Смартфоны".')


    """Методы"""

    def select_smartphones(self):
        self.check_u = "https://www.dns-shop.ru/catalog/af47fe7c3bae7fd7/smartfony-i-gadzhety/"

        Logger.add_start_step(method='select_smartphones')
        self.get_current_url()
        self.check_url(self.check_u)
        self.click_smartphones_button()
        Logger.add_end_step(url=self.driver.current_url, method='select_smartphones')