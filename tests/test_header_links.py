import pytest
from pages.main_page import MainPage
from pages.header import Header
from data.data import TestData

class TestHeaderLinks:

    def test_scooter_logo_redirects_to_home(self, driver):
        page = MainPage(driver)
        page.go_to_url(TestData.BASE_URL)

        header = Header(driver)
        header.click_scooter_logo()

        assert header.is_home_page_opened()

    def test_yandex_logo_opens_dzen(self, driver):
        page = MainPage(driver)
        page.go_to_url(TestData.BASE_URL)

        header = Header(driver)
        header.click_yandex_logo()

        # Всё перенесено в BasePage
        header.switch_to_new_tab()

        assert header.is_dzen_page_opened()

