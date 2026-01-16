from selenium.webdriver.common.by import By

class HeaderLocators:
    SCOOTER_LOGO = (By.XPATH, "//div[contains(@class, 'Header_Logo')]/a")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")
    YANDEX_IFRAME = (By.XPATH, "//iframe[contains(@aria-label, 'Поиск Яндекса')]")
