import pytest
import allure
from selenium import webdriver

from pages.calculator_page import CalculatorPage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.feature("Калькулятор")
@allure.story("Выполнение сложения")
def test_slow_calculator_sum(driver):
    page = CalculatorPage(driver)

    with allure.step("Открытие страницы калькулятора"):
        page.open()

    with allure.step("Установка задержки вычислений 30 мс"):
        page.set_delay("30")

    with allure.step("Ввод чисел и операций: 7 + 8 ="):
        page.press_button("7")
        page.press_button("+")
        page.press_button("8")
        page.press_button("=")

    with allure.step("Получение результата вычислений"):
        result = page.get_result()

    with allure.step(f"Проверка результата: ожидается '15', получено '{result}'"):
        assert result == "15", f"Ожидаемый результат '15', но получен '{result}'"