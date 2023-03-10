import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.main_page import Main_page
from pages.smartphones_phototechnics_page import Smartphones_phototechnics_page
from pages.smartphones_gadgets_page import Smartphones_gadgets_page
from pages.smartphones_page import Smartphones_page
from pages.cart_page import Cart_page


CHROMEDRIVE_PATH = "utils/chromedriver.exe"


@pytest.mark.run(order=1)
@allure.description("Покупка смартфона №1")
def test_buy_smartphone_1(set_group, set_up):  # Тест №1 - выбор самого популярного смартфона производителя Xiaomi стоимостью от 10000 до 50000, на который есть обзор, скидка, а также подтверждение его надёжности
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    g = Service(CHROMEDRIVE_PATH)
    driver = webdriver.Chrome(options=options, service=g)

    main_page = Main_page(driver)
    main_page.select_smartphones_phototechnics()

    smartphones_phototechnics_page = Smartphones_phototechnics_page(driver)
    smartphones_phototechnics_page.select_smartphones_gadgets()

    smartphones_gadgets_page = Smartphones_gadgets_page(driver)
    smartphones_gadgets_page.select_smartphones()

    smartphones_page = Smartphones_page(driver)
    smartphone_name, smartphone_price = smartphones_page.select_smartphone_1()
    smartphone_price = smartphone_price.replace(' ', '')[0:5]
    smartphone_name = smartphone_name[0:smartphone_name.find('[')].replace(' ', '')

    cart_page = Cart_page(driver, smartphone_name, smartphone_price)
    cart_page.finish()

    driver.quit()


@pytest.mark.run(order=2)
@allure.description("Покупка смартфона №2")
def test_buy_smartphone_2(set_group, set_up):  # Тест №2 - выбор смартфона с лучшей оценкой производителя realme стоимостью от 10000 до 50000, на который есть обзор, скидка, а также подтверждение его надёжности
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    g = Service(CHROMEDRIVE_PATH)
    driver = webdriver.Chrome(options=options, service=g)

    main_page = Main_page(driver)
    main_page.select_smartphones_phototechnics()

    smartphones_phototechnics_page = Smartphones_phototechnics_page(driver)
    smartphones_phototechnics_page.select_smartphones_gadgets()

    smartphones_gadgets_page = Smartphones_gadgets_page(driver)
    smartphones_gadgets_page.select_smartphones()

    smartphones_page = Smartphones_page(driver)
    smartphone_name, smartphone_price = smartphones_page.select_smartphone_2()
    smartphone_price = smartphone_price.replace(' ', '')[0:5]
    smartphone_name = smartphone_name[0:smartphone_name.find('[')].replace(' ', '')

    cart_page = Cart_page(driver, smartphone_name, smartphone_price)
    cart_page.finish()

    driver.quit()