import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage


class DynamicTablePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        self.page_url = 'http://uitestingplayground.com/dynamictable'
        self.chrome_process_cpu_value = (By.XPATH, '//*[@role="cell"][text()="Chrome"]/../*[@role="cell"][contains(text(), "%")]')
        self.chrome_process_cpu_value_yellow = (By.XPATH, '//p[@class="bg-warning"]')

    @allure.step(r"Получить значение cpu в таблице")
    def get_value_chrome_process_cpu(self) -> str:
        return self.get_text(self.chrome_process_cpu_value)

    @allure.step(r"Получить значение cpu в жёлтой рамочке")
    def get_value_chrome_process_cpu_yellow(self) -> str:
        return self.get_text(self.chrome_process_cpu_value_yellow)[12:]