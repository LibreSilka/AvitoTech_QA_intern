from base_page import BasePage
from locators import AdvertisementsLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AdvertisementsPage(BasePage):
    """Страница объявлений"""

    BASE_URL = "http://tech-avito-intern.jumpingcrab.com/advertisements/"

    def open(self):
        super().open(self.BASE_URL)

    def create_advertisement(self, ad_data):
        """Создание объявления"""
        self.click(AdvertisementsLocators.CREATE_BUTTON)

        self.send_keys((By.NAME, "name"), ad_data["title"])
        self.send_keys((By.NAME, "price"), ad_data["price"])
        self.send_keys((By.NAME, "description"), ad_data["description"])
        self.send_keys((By.NAME, "imageUrl"), ad_data["image"])

        self.click(AdvertisementsLocators.SAVE_BUTTON)

    def search_advertisement(self, title):
        """Поиск объявления"""
        self.send_keys(AdvertisementsLocators.SEARCH_INPUT, title)
        self.send_keys(AdvertisementsLocators.SEARCH_INPUT, Keys.RETURN)

        return self.wait_for_element(AdvertisementsLocators.AD_TITLE).is_displayed()

    def edit_advertisement(self, new_title):
        """Редактирование объявления"""
        self.click(AdvertisementsLocators.AD_LINK)
        self.click(AdvertisementsLocators.EDIT_BUTTON)

        self.send_keys((By.NAME, "name"), new_title)

        self.click(AdvertisementsLocators.SAVE_EDIT_BUTTON)

        return self.wait_for_element(AdvertisementsLocators.UPDATED_TITLE(new_title)).is_displayed()
