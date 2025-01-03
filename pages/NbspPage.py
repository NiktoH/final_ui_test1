import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage


class NbspPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        self.page_url = 'http://uitestingplayground.com/nbsp'
        self.button = (By.XPATH, '//button[normalize-space(translate(., "\u00A0", " "))="My Button"]')

    @allure.step(r"Получить текст кнопки")
    def get_btn_text(self) -> str:
        return self.get_text(self.button)

    @allure.step(r"Проверить наличие кнопки")
    def check_btn(self):
        return self.get_element_displayed(self.button)