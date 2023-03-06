from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = "https://www.dns-shop.ru/"
    

    """Локаторы"""

    smartphones_phototechnics_button_locator = "//a[@href='/catalog/17a890dc16404e77/smartfony-i-fototexnika/'][@class='catalog-menu__root-item-info catalog-menu__root-item-title']"


    """Геттеры"""

    def get_smartphones_phototechnics_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.smartphones_phototechnics_button_locator)))


    """Действия"""

    def click_smartphones_phototechnics_button(self):
        self.get_smartphones_phototechnics_button().click()
        print('Нажата кнопка "Смартфоны и фототехника".')


    """Методы"""

    def select_smartphones_phototechnics(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.check_url(self.url)
        self.click_smartphones_phototechnics_button()