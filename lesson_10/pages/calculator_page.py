import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class CalculatorPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver):
        """
        Инициализирует экземпляр страницы калькулятора.

        Параметры:
        driver: веб‑драйвер Selenium (например, ChromeDriver), используемый для взаимодействия с браузером.
        """
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.screen = (By.CLASS_NAME, "screen")

    @allure.step("Открыть страницу калькулятора")
    def open(self):
        """
        Открывает страницу калькулятора по указанному URL.

        Параметры: отсутствуют.
        Возвращаемое значение: отсутствует.
        """
        self.driver.get(self.URL)

    @allure.step("Установить задержку: {seconds} секунд")
    def set_delay(self, seconds: str):
        """
        Устанавливает задержку в поле ввода калькулятора.

        Параметры:
        seconds (str): строка, представляющая количество секунд задержки.

        Возвращаемое значение: отсутствует.
        """
        field = self.driver.find_element(*self.delay_input)
        field.clear()
        field.send_keys(seconds)

    @allure.step("Нажать кнопку: {value}")
    def press_button(self, value: str):
        """
        Нажимает кнопку с указанным значением на калькуляторе.

        Параметры:
        value (str): текст на кнопке, которую нужно нажать (например, '7', '+', '=').

        Возвращаемое значение: отсутствует.
        """
        btn = self.driver.find_element(By.XPATH, f"//span[text()='{value}']")
        btn.click()

    @allure.step("Получить результат (таймаут: {timeout} сек)")
    def get_result(self, timeout: int = 70) -> str:
        """
        Ожидает отображения результата на экране калькулятора и возвращает его.

        Параметры:
        timeout (int): максимальное время ожидания результата в секундах (по умолчанию — 70 с).

        Возвращаемое значение:
        str: текст, отображаемый на экране калькулятора (результат вычислений).
        """
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(*self.screen).text == "15"
        )
        return self.driver.find_element(*self.screen).text