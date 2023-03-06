from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Smartphones_phototechnics_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Локаторы"""

    smartphones_gadgets_button_locator = "//a[@href='/catalog/af47fe7c3bae7fd7/smartfony-i-gadzhety/'][@class='subcategory__item ui-link ui-link_blue']"


    """Геттеры"""

    def get_smartphones_gadgets_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.smartphones_gadgets_button_locator)))


    """Действия"""

    def click_smartphones_gadgets_button(self):
        self.get_smartphones_gadgets_button().click()
        print('Нажата кнопка "Смартфоны и гаджеты".')


    """Методы"""

    def select_smartphones_gadgets(self):
        self.check_u = "https://www.dns-shop.ru/catalog/17a890dc16404e77/smartfony-i-fototexnika/"

        self.get_current_url()
        self.check_url(self.check_u)
        self.click_smartphones_gadgets_button()