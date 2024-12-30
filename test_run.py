import time
import allure

from selenium.webdriver.support.wait import WebDriverWait
from pages.BasePage import BasePage
from pages.DynamicTablePage import DynamicTablePage
from pages.LoadDelayPage import LoadDelayPage
from pages.NbspPage import NbspPage
from pages.ProgressBarPage import ProgressBarPage
from pages.MainPage import MainPage
from pages.TextInputPage import TextInputPage


@allure.title(r"Проверка заданий с прогрессбаром")
def test_1_progress_bar(driver):
    driver.get('http://uitestingplayground.com/progressbar')

    progress_bar_page = ProgressBarPage(driver)
    progress_bar_page.click_start_button()
    progress_bar_page.check_progressbar_percent()
    assert progress_bar_page.check_result_number() < 5, "Result !< 5"
    while progress_bar_page.check_duration_number() >= 17000:
        progress_bar_page.click_start_button()
        progress_bar_page.check_progressbar_percent()
        assert progress_bar_page.check_result_number() < 5, "Result !< 5"
    else:
        return True

@allure.title(r"Проверка загрузки страницы Load Delay")
def test_2_load_delay(driver):
    driver.get('http://uitestingplayground.com/')
    main_page = MainPage(driver)
    main_page.click_ld()

    load_page = LoadDelayPage(driver)
    load_page.wait_load_delay()
    assert load_page.check_load_delay_btn() == "Button Appearing After Delay", "Кнопка Button Appearing After Delay не найдена"

@allure.title(r"Проверка ввода названия кнопки")
def test_3_text_input(driver):
    driver.get('http://uitestingplayground.com/textinput')

    text_input_page = TextInputPage(driver)
    assert text_input_page.check_btn_name() == "Button That Should Change it's Name Based on Input Value", "Не найдена кнопка"
    text_input_page.fill_new_btn_name()
    text_input_page.click_new_btn()
    assert text_input_page.check_btn_name() != "Button That Should Change it's Name Based on Input Value", "Название не поменялось"

@allure.title(r"Проверка значения Chrome cpu")
def test_4_dynamic_table(driver):
    driver.get('http://uitestingplayground.com/dynamictable')
    time.sleep(10)

    dynamic_table_page = DynamicTablePage(driver)
    assert dynamic_table_page.get_value_chrome_process_cpu() == dynamic_table_page.get_value_chrome_process_cpu_yellow(), "yellow cpu value != chrome cpu value"

@allure.title(r"Проверка локатора non-spacing текста")
def test_5_nbsp(driver):
    driver.get('http://uitestingplayground.com/nbsp')

    nbsp_page = NbspPage(driver)
    assert nbsp_page.get_btn_text() == "My Button"
    assert nbsp_page.check_btn()

