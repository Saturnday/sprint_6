import pytest
from pages.main_page import MainPage
from pages.header import Header
from data.data import TestData
from selenium.webdriver.support.ui import WebDriverWait

class TestHeaderLinks:

    def test_scooter_logo_redirects_to_home(self, driver):
        page = MainPage(driver)
        page.go_to_url(TestData.BASE_URL)

        header = Header(driver)
        header.click_scooter_logo()

        assert TestData.SCOOTER_HOME_TEXT in driver.page_source

    def test_yandex_logo_opens_dzen(self, driver):
        page = MainPage(driver)
        page.go_to_url(TestData.BASE_URL)

        header = Header(driver)
        header.click_yandex_logo()

        # Переключаемся на новую вкладку
        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(driver.window_handles[-1])

        label = header.get_yandex_iframe_label()
        assert "Поиск Яндекса" in label
