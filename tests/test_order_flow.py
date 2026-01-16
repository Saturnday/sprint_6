import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.order_test_data import OrderData
from locators.main_page_locators import MainPageLocators
from data.data import TestData


class TestOrderPage:
    @pytest.mark.parametrize('locator, order_data', [
        (MainPageLocators.ORDER_BUTTON_UP, OrderData.ORDER_DATA_1),
        (MainPageLocators.ORDER_BUTTON_DOWN, OrderData.ORDER_DATA_2),
    ])
    def test_create_order(self, driver, locator, order_data):
        page = OrderPage(driver)
        page.go_to_url(TestData.BASE_URL)
        page.click_to_element(locator)
        page.set_order(order_data)
        assert page.check_order()