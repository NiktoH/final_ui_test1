import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage


class LoadDelayPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        self.page_url = 'http://uitestingplayground.com/loaddelay'
        self.load_delay_btn = (By.XPATH, '//button[contains(text(), "Button Appearing After Delay")]')
        self.wait = WebDriverWait(driver, timeout=2)

    @allure.step(r"Проверить, что кнопка Button Appearing After Delay отображается")
    def check_load_delay_btn(self):
        return self.get_text(self.load_delay_btn)

    @allure.step(r"Ждать, пока страница не загрузится")
    def wait_load_delay(self):
        self.wait.until(lambda d: self.check_load_delay_btn())