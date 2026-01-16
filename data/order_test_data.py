from locators.order_page_locators import OrderPageLocators

class OrderData():
    ORDER_DATA_1 = {
        'name': 'Иван',
        'last_name': 'Иванов',
        'address': 'г. Москва, ул. Пушкина, д. 1',
        'station_locator': OrderPageLocators.METRO_FIELD,
        'phone': '+79991234567',
        'date': '10.07.2025',
        'rent_time': 'сутки',
        'color': 'black',
        'comment': 'Позвонить за 5 минут',
        'button_locator': OrderPageLocators.ORDER_BUTTON,
    }

    ORDER_DATA_2 = {
        'name': 'Петр',
        'last_name': 'Петров',
        'address': 'г. Москва, ул. Ленина, д. 2',
        'station_locator': OrderPageLocators.METRO_FIELD,
        'phone': '+79997654321',
        'date': '12.07.2025',
        'rent_time': 'двое суток',
        'color': 'gray',
        'comment': '',
        'button_locator': OrderPageLocators.ORDER_BUTTON,
    }
