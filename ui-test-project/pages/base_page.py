from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    TIMEOUT = 80

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_page(self, driver):
        driver.get(self.context.base_url+self.URL)

    def wait_element_to_be_clickable(self, locator, element):
        return WebDriverWait(self.driver, self.TIMEOUT).until(EC.element_to_be_clickable((locator, element)))

    def wait_element_visibility(self, locator, element):
        return WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located((locator, element)))

    def click_in_element(self, locator, element):
        button = self.wait_element_to_be_clickable(locator, element)
        button.click()

    def write_in_element(self, locator, element, text):
        element = self.wait_element_to_be_clickable(locator, element)
        element.send_keys(text)
