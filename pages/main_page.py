import allure
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import Logger


"""Локаторы"""

SMARTPHONES_PHOTOTECHNICS_BUTTON_LOCATOR = "//a[@href='/catalog/17a890dc16404e77/smartfony-i-fototexnika/'][@class='catalog-menu__root-item-info catalog-menu__root-item-title']"


"""Класс начальной страницы"""

class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = "https://www.dns-shop.ru/"


    """Геттеры"""

    def get_smartphones_phototechnics_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, SMARTPHONES_PHOTOTECHNICS_BUTTON_LOCATOR)))


    """Действия"""

    def click_smartphones_phototechnics_button(self):
        self.get_smartphones_phototechnics_button().click()
        print('Нажата кнопка "Смартфоны и фототехника".')


    """Методы"""

    def select_smartphones_phototechnics(self):
        with allure.step('select_smartphones_phototechnics'):
            Logger.add_start_step(method='select_smartphones_phototechnics')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.check_url(self.url)
            self.click_smartphones_phototechnics_button()
            Logger.add_end_step(url=self.driver.current_url, method='select_smartphones_phototechnics')