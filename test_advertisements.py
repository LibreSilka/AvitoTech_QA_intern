import pytest
from advertisements_page import AdvertisementsPage

@pytest.fixture(scope="module")
def advertisements_page(driver):
    """Фикстура для страницы объявлений"""
    return AdvertisementsPage(driver)

@pytest.fixture(scope="session")
def unique_ad_data():
    """Фикстура для уникальных данных объявления"""
    return {
        "title": "Test Ad 12345",
        "price": "100",
        "description": "Test Description",
        "image": "path/to/image.jpg"
    }

def test_create_advertisement(advertisements_page, unique_ad_data):
    """Тест создания объявления"""
    advertisements_page.open()
    advertisements_page.create_advertisement(unique_ad_data)

def test_search_advertisement(advertisements_page, unique_ad_data):
    """Тест поиска объявления"""
    advertisements_page.open()
    assert advertisements_page.search_advertisement(unique_ad_data["title"]), "Объявление не найдено"

def test_edit_advertisement(advertisements_page, unique_ad_data):
    """Тест редактирования объявления"""
    advertisements_page.open()
    new_title = f"Updated {unique_ad_data['title']}"
    assert advertisements_page.edit_advertisement(new_title), "Редактирование не удалось"
