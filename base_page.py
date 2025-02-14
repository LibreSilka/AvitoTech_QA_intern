from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Базовый класс для всех страниц"""
    TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        """Открытие страницы"""
        self.driver.get(url)

    def wait_for_element(self, locator):
        """Ожидание появления элемента"""
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator):
        """Клик по элементу"""
        element = self.wait_for_element(locator)
        element.click()

    def send_keys(self, locator, text):
        """Ввод текста в поле"""
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)