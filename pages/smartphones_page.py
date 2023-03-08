import time
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"""Локаторы"""

MIN_PRICE_FIELD_LOCATOR = "//input[@class='ui-input-small__input ui-input-small__input_list'][@placeholder='от 2 999']"
MAX_PRICE_FIELD_LOCATOR = "//input[@class='ui-input-small__input ui-input-small__input_list'][@placeholder='до 169 299']"
DISCOUNTS_CHECKBOX_BUTTON_LOCATOR = "//label[@class='ui-checkbox ui-checkbox_list']//input[@value='tovarysoskidkoj']//following-sibling::span"
XIAOMI_CHECKBOX_BUTTON_LOCATOR = "//label[@class='ui-checkbox ui-checkbox_list']//input[@value='xiaomi']//following-sibling::span"
REALME_CHECKBOX_BUTTON_LOCATOR = "//label[@class='ui-checkbox ui-checkbox_list']//input[@value='realme']//following-sibling::span"
RELIABLE_MODELS_CHECKBOX_BUTTON_LOCATOR = "//div[@data-id='rely']//label[@class='ui-checkbox']//input[@type='checkbox']//following-sibling::span"
REVIEW_CHECKBOX_BUTTON_LOCATOR = "//div[@data-id='review']//label[@class='ui-checkbox']//input[@type='checkbox']//following-sibling::span"
APPLY_FILTERS_BUTTON_LOCATOR = "//button[@data-role='filters-submit']"
SORTING_METHOD_BUTTON_LOCATOR = "//div[@data-id='order']/a[@class='ui-link ui-link_blue']/span[@class='top-filter__selected']"
POPULAR_CHECKBOX_BUTTON_LOCATOR = "//label[@class='ui-radio__item']/span[contains(text(), 'Сначала популярные')]"
BEST_SCORE_CHECKBOX_BUTTON_LOCATOR = "//label[@class='ui-radio__item']/span[contains(text(), 'Сначала с лучшей оценкой')]"
FIRST_SMARTPHONE_NAME_LOCATOR = "/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/a/span"
FIRST_SMARTPHONE_PRICE_LOCATOR = "/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[4]/div/div[1]"
FIRST_SMARTPHONE_BUY_BUTTON_LOCATOR = "/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[4]/button[2]"
TO_CART_BUTTON_LOCATOR = "/html/body/div[1]/header/div[1]/nav/div/div[3]/div[1]/div/div/div/div[2]/div[2]/button[2]/span"

MIN_PRICE_1 = "10000"
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
    
    def get_discounts_checkbox_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, DISCOUNTS_CHECKBOX_BUTTON_LOCATOR)))
    
    def get_xiaomi_checkbox_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, XIAOMI_CHECKBOX_BUTTON_LOCATOR)))
    
    def get_realme_checkbox_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, REALME_CHECKBOX_BUTTON_LOCATOR)))
    
    def get_reliable_models_checkbox_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, RELIABLE_MODELS_CHECKBOX_BUTTON_LOCATOR)))
    
    def get_review_checkbox_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, REVIEW_CHECKBOX_BUTTON_LOCATOR)))
    
    def get_apply_filters_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, APPLY_FILTERS_BUTTON_LOCATOR)))
    
    def get_sorting_method_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, SORTING_METHOD_BUTTON_LOCATOR)))
    
    def get_popular_checkbox_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, POPULAR_CHECKBOX_BUTTON_LOCATOR)))
    
    def get_best_score_checkbox_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, BEST_SCORE_CHECKBOX_BUTTON_LOCATOR)))
    
    def get_first_smartphone_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, FIRST_SMARTPHONE_NAME_LOCATOR)))
    
    def get_first_smartphone_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, FIRST_SMARTPHONE_PRICE_LOCATOR)))
    
    def get_first_smartphone_buy_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, FIRST_SMARTPHONE_BUY_BUTTON_LOCATOR)))
    
    def get_to_cart_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, TO_CART_BUTTON_LOCATOR)))


    """Действия"""

    def fill_min_price_field(self, data):
        min_price_field = self.get_min_price_field()
        self.move_to_element(min_price_field, self.driver)
        min_price_field.send_keys(data)
        print('Поле минимальной стоимости заполнено.')
    
    def fill_max_price_field(self, data):
        max_price_field = self.get_max_price_field()
        self.move_to_element(max_price_field, self.driver)
        max_price_field.send_keys(data)
        print('Поле максимальной стоимости заполнено.')
    
    def click_discounts_checkbox_button(self):
        discounts_checkbox_button = self.get_discounts_checkbox_button()
        self.move_to_element(discounts_checkbox_button, self.driver)
        discounts_checkbox_button.click()
        print('Выбран фильтр "Скидки и предложения".')
    
    def click_xiaomi_checkbox_button(self):
        xiaomi_checkbox_button = self.get_xiaomi_checkbox_button()
        self.move_to_element(xiaomi_checkbox_button, self.driver)
        xiaomi_checkbox_button.click()
        print('Выбран производитель "Xiaomi".')

    def click_realme_checkbox_button(self):
        realme_checkbox_button = self.get_realme_checkbox_button()
        self.move_to_element(realme_checkbox_button, self.driver)
        realme_checkbox_button.click()
        print('Выбран производитель "realme".')
    
    def click_reliable_models_checkbox_button(self):
        reliable_models_checkbox_button = self.get_reliable_models_checkbox_button()
        self.move_to_element(reliable_models_checkbox_button, self.driver)
        reliable_models_checkbox_button.click()
        print('Выбран фильтр "Надёжные модели".')
    
    def click_review_checkbox_button(self):
        review_checkbox_button = self.get_review_checkbox_button()
        self.move_to_element(review_checkbox_button, self.driver)
        review_checkbox_button.click()
        print('Выбран фильтр "Есть обзор".')
    
    def click_apply_filters_button(self):
        apply_filters_button = self.get_apply_filters_button()
        self.move_to_element(apply_filters_button, self.driver)
        apply_filters_button.click()
        print('Нажата кнопка "Применить".')
    
    def click_sorting_method_button(self):
        sorting_method_button = self.get_sorting_method_button()
        self.move_to_element(sorting_method_button, self.driver)
        sorting_method_button.click()
        print('Нажата кнопка выбора метода сортировки.')
    
    def click_popular_checkbox_button(self):
        popular_checkbox_button = self.get_popular_checkbox_button()
        self.move_to_element(popular_checkbox_button, self.driver)
        popular_checkbox_button.click()
        print('Выбран метод сортировки "Сначала популярные".')

    def click_best_score_checkbox_button(self):
        best_score_checkbox_button = self.get_best_score_checkbox_button()
        self.move_to_element(best_score_checkbox_button, self.driver)
        best_score_checkbox_button.click()
        print('Выбран метод сортировки "Сначала с лучшей оценкой".')

    def click_first_smartphone_buy_button(self):
        first_smartphone_buy_button = self.get_first_smartphone_buy_button()
        self.move_to_element(first_smartphone_buy_button, self.driver)
        first_smartphone_buy_button.click()
        print('Нажата кнопка "Купить".')
    
    def click_to_cart_button(self):
        to_cart_button = self.get_to_cart_button()
        self.move_to_element(to_cart_button, self.driver)
        to_cart_button.click()
        print('Нажата кнопка "В корзину".')


    """Методы"""

    def select_smartphone_1(self):
        self.check_u = "https://www.dns-shop.ru/catalog/17a8a01d16404e77/smartfony/"

        self.load_page()
        self.get_current_url()
        self.check_url(self.check_u)
        self.click_review_checkbox_button()
        self.fill_min_price_field(MIN_PRICE_1)
        self.fill_max_price_field(MAX_PRICE_1)
        self.click_discounts_checkbox_button()
        self.click_xiaomi_checkbox_button()
        self.click_reliable_models_checkbox_button()
        self.click_apply_filters_button()
        self.click_sorting_method_button()
        self.click_popular_checkbox_button()
        time.sleep(2)
        first_smartphone_name, first_smartphone_price = self.get_first_smartphone_name().text, self.get_first_smartphone_price().text
        self.click_first_smartphone_buy_button()
        self.click_to_cart_button()

        return first_smartphone_name, first_smartphone_price
    
    def select_smartphone_2(self):
        self.check_u = "https://www.dns-shop.ru/catalog/17a8a01d16404e77/smartfony/"

        self.load_page()
        self.get_current_url()
        self.check_url(self.check_u)
        self.click_review_checkbox_button()
        self.fill_min_price_field(MIN_PRICE_1)
        self.fill_max_price_field(MAX_PRICE_1)
        self.click_discounts_checkbox_button()
        self.click_realme_checkbox_button()
        self.click_reliable_models_checkbox_button()
        self.click_apply_filters_button()
        self.click_sorting_method_button()
        self.click_best_score_checkbox_button()
        time.sleep(2)
        first_smartphone_name, first_smartphone_price = self.get_first_smartphone_name().text, self.get_first_smartphone_price().text
        self.click_first_smartphone_buy_button()
        self.click_to_cart_button()

        return first_smartphone_name, first_smartphone_price