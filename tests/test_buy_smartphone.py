from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.main_page import Main_page


CHROMEDRIVE_PATH = "utils/chromedriver.exe"


def test_buy_smartphone():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    g = Service(CHROMEDRIVE_PATH)
    driver = webdriver.Chrome(options=options, service=g)

    main_page = Main_page(driver)
    main_page.select_smartphone()