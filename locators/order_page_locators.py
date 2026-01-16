from selenium.webdriver.common.by import By

class OrderPageLocators:
    #first page
    NAME_LOCATOR = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_LOCATOR = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_LOCATOR = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']") 
    METRO_SELECTED = (By.XPATH, "//button[@value='1']")
    PHONE_LOCATOR = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    #second page
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_SELECTED = (By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='13']")
    RENT_DROPDOWN = (By.CLASS_NAME, "Dropdown-arrow")
    RENT_OPTION = (By.XPATH, "//div[text()='сутки']") 
    COLOR_CHECKBOX_BLACK = (By.ID, "black")
    COLOR_CHECKBOX_GRAY = (By.ID, "grey")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    
    SUCCESS_POPUP = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
