import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage


class TextInputPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        self.page_url = 'http://uitestingplayground.com/textinput'
        self.new_button_name = (By.XPATH, '//div[@class="form-group"]//input[@id="newButtonName"]')
        self.new_btn = (By.XPATH, '//div[@class="form-group"]//button[@id="updatingButton"]')
        self.origin_btn_name = (By.XPATH, '//div[@class="form-group"]//button[@id="updatingButton"]')

    @allure.step(r"Ввести имя для новой кнопки")
    def fill_new_btn_name(self):
        self.fill_field(self.new_button_name, 'MyNewButton')

    @allure.step(r"Нажать на новую кнопку")
    def click_new_btn(self):
        self.click_element(self.new_btn)

    @allure.step(r"Получить текст кнопки")
    def check_btn_name(self) -> str:
       return self.get_text(self.new_btn)