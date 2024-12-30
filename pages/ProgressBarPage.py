import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage


class ProgressBarPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        self.page_url = 'http://uitestingplayground.com/progressbar'
        self.start_btn = (By.XPATH, '//*[@id="startButton"]')
        self.progress_bar = (By.XPATH, '//div[@id="progressBar"]')
        self.stop_btn = (By.XPATH, '//*[@id="stopButton"]')
        self.result_nmb = (By.XPATH, '//div[@id="content"]//p[@id="result"]')

    @allure.step(r"Кликнуть по кнопке Start")
    def click_start_button(self) -> None:
        self.click_element(self.start_btn)

    @allure.step(r"Проверить, что прогрессбар стал 75%")
    def check_progressbar_percent(self) -> None:
        while True:
            value = self.get_text(self.progress_bar)
            if value == "75%":
                with allure.step(r"Кликаем по кнопке Stop"):
                    self.click_element(self.stop_btn)
                break

    @allure.step(r"Проверить, что Result < 5")
    def check_result_number(self) -> int:
        return int(self.get_text(self.result_nmb)[8])

    @allure.step(r"Проверить, что Duration < 17000")
    def check_duration_number(self) -> int:
        return int(self.get_text(self.result_nmb)[21:])




