import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):

    @allure.step('Заполняем данные клиента')
    def fill_client_info(self, data):
        self.add_text_to_element(OrderPageLocators.NAME_LOCATOR, data['name'])
        self.add_text_to_element(OrderPageLocators.LAST_NAME_LOCATOR, data['last_name'])
        self.add_text_to_element(OrderPageLocators.ADDRESS_LOCATOR, data['address'])
        self.click_to_element(data['station_locator'])
        self.find_element_with_wait(OrderPageLocators.METRO_SELECTED)
        self.click_to_element(OrderPageLocators.METRO_SELECTED)
        self.add_text_to_element(OrderPageLocators.PHONE_LOCATOR, data['phone'])
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполняем данные аренды')
    def fill_rent_info_and_submit(self, data):
        self.add_text_to_element(OrderPageLocators.DATE_FIELD, data['date'])
        self.click_to_element(OrderPageLocators.RENT_DROPDOWN)
        self.click_to_element(OrderPageLocators.RENT_OPTION)

        if data['color'] == 'black':
            self.click_to_element(OrderPageLocators.COLOR_CHECKBOX_BLACK)
        elif data['color'] == 'gray':
            self.click_to_element(OrderPageLocators.COLOR_CHECKBOX_GRAY)

        self.add_text_to_element(OrderPageLocators.COMMENT_FIELD, data['comment'])
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)
        self.click_to_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step('Оформляем заказ полностью')
    def set_order(self, data):
        self.fill_client_info(data)
        self.fill_rent_info_and_submit(data)

    @allure.step('Проверяем, что заказ успешно создан')
    def check_order(self):
        success_text = self.get_text(OrderPageLocators.SUCCESS_POPUP)
        return "Заказ оформлен" in success_text
