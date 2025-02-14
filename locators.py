from selenium.webdriver.common.by import By

class AdvertisementsLocators:
    CREATE_BUTTON = (By.XPATH, "//button[text()='Создать']")
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Поиск по объявлениям']")
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")
    SAVE_EDIT_BUTTON = (By.CSS_SELECTOR, "svg[style='cursor: pointer;']")
    AD_TITLE = (By.XPATH, "//h4[starts-with(text(), 'Test Ad')]")
    EDIT_BUTTON = (By.CSS_SELECTOR, "svg[style='cursor: pointer;']")
    UPDATED_TITLE = lambda title: (By.XPATH, f"//h2[contains(text(), '{title}')]")
    AD_LINK = (By.XPATH, "(//a[starts-with(@href, '/advertisements')])[2]")
