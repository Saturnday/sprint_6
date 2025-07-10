from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(self.driver, self.timeout)

    def go_to_url(self, url):
        self.driver.get(url)
        
    def find_element_with_wait(self, locator):
        self.wait.until(
            EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_to_element(self, some):
        self.wait.until(
            EC.element_to_be_clickable(some))
        self.driver.find_element(*some).click()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text(self, locator): 
        return self.find_element_with_wait(locator).text
    
    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return method, locator
    
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def wait_for_element(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def my_drag_and_drop(self, locator_from, locator_to):
        elem_from = self.find_element_with_wait(locator_from)
        elem_to = self.find_element_with_wait(locator_to)
        
        self.driver.drag_and_drop(elem_from, elem_to).perform()
    
    def switch_to_new_tab(self):
        # Ждём появления новой вкладки
        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        
        # Ждём, пока страница в новой вкладке полностью загрузится (DOM готов)
        WebDriverWait(self.driver, 20).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )


    
    