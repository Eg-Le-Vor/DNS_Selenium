from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.main_page import Main_page
from pages.smartphones_phototechnics_page import Smartphones_phototechnics_page
from pages.smartphones_gadgets_page import Smartphones_gadgets_page


CHROMEDRIVE_PATH = "utils/chromedriver.exe"


def test_buy_smartphone(set_group, set_up):
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

    # driver.quit()