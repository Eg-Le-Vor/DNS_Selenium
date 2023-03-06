import datetime


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