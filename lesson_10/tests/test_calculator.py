import pytest
from selenium import webdriver

from pages.calculator_page import CalculatorPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@allure.title("Тестирование калькулятора: 7+8=15")
@allure.description("Тестирование проверяет работоспособность калькулятора")
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Калькулятор")
def test_slow_calculator_sum(driver):
    page = CalculatorPage(driver)

    with allure.step("Открытие страницы калькулятора"):

    page.open()
    page.set_delay("45")

    page.press_button("7")
    page.press_button("+")
    page.press_button("8")
    page.press_button("=")

    result = page.get_result(46)
    assert result == "15"