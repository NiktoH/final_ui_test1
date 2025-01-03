import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        self.page_url = 'http://uitestingplayground.com/'
        self.progressbar_page = (By.CSS_SELECTOR, '[href="/progressbar"]')
        self.load_delay_page = (By.CSS_SELECTOR, '[href="/loaddelay"]')
        self.text_input_page = (By.CSS_SELECTOR, '[href="/textinput"]')
        self.dynamic_table_page = (By.CSS_SELECTOR, '[href="/dynamictable"]')
        self.nbsp_page = (By.CSS_SELECTOR, '[href="/nbsp"]')

    @allure.step(r"Кликнуть по ссылке Load Delay")
    def click_ld(self):
        self.click_element(self.load_delay_page)