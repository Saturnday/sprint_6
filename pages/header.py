import allure
from pages.base_page import BasePage
from locators.header_locators import HeaderLocators

class Header(BasePage):
    @allure.step('Клик на Скутер')
    def click_scooter_logo(self):
        self.click_to_element(HeaderLocators.SCOOTER_LOGO)
        
    @allure.step('Клик на Яндекс')
    def click_yandex_logo(self):
        self.click_to_element(HeaderLocators.YANDEX_LOGO)

    @allure.step('Переход на новую вкладку')
    def get_yandex_iframe_label(self):
        iframe = self.wait_for_element(HeaderLocators.YANDEX_IFRAME)
        return iframe.get_attribute("aria-label")
