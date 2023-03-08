import time
import datetime
from selenium.webdriver.common.action_chains import ActionChains


"""Базовый класс необходимый для создания любого класса страницы"""

class Base():

    def __init__(self, driver):
        self.driver = driver
        self.check_u = ""


    """Метод получения текущего URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'\nТекущий URL: {get_url}.', end=' ')
        

    """Метод проверки URL"""

    def check_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('URL корректный.')


    """Метод создания скриншота"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        screenshot_name = "screenshot" + now_date + ".png"
        self.driver.save_screenshot(f'../screenshots/{screenshot_name}')
        print('Скриншот текущей страницы сохранён.')


    """Метод полной прогрузки страницы"""

    def load_page(self):
        time.sleep(1)
        counter = 100
        for _ in range(20):
            time.sleep(0.02)
            self.driver.execute_script(f'window.scrollTo(0, {counter})')
            counter += 100
        time.sleep(1)
    

    """Метод перемещения страницы к указанному элементу"""

    def move_to_element(self, element_locator, current_driver):
        action = ActionChains(current_driver)
        action.move_to_element(element_locator).perform()