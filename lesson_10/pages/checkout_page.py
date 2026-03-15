import allure
from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        """
        Инициализирует экземпляр страницы оформления заказа (Checkout).

        Параметры:
        driver: веб‑драйвер Selenium (например, ChromeDriver), используемый для взаимодействия с браузером.
        """
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Заполнить форму оформления заказа: имя — {first_name}, фамилия — {last_name}, почтовый индекс — {postal_code}")
    def fill_form(self, first_name: str, last_name: str, postal_code: str):
        """
        Заполняет форму оформления заказа на странице Checkout данными пользователя.

        Параметры:
        first_name (str): имя пользователя, которое будет введено в поле «First Name».
        last_name (str): фамилия пользователя, которая будет введена в поле «Last Name».
        postal_code (str): почтовый индекс, который будет введён в соответствующее поле.

        Возвращаемое значение: отсутствует.
        """
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.postal_code).send_keys(postal_code)

    @allure.step("Нажать кнопку Continue")
    def click_continue(self):
        """
        Нажимает кнопку Continue для перехода к следующему этапу оформления заказа.

        Параметры: отсутствуют.
        Возвращаемое значение: отсутствует.
        """
        self.driver.find_element(*self.continue_button).click()

    @allure.step("Получить итоговую сумму заказа")
    def get_total(self) -> str:
        """
        Получает итоговую сумму заказа, отображаемую на странице.

        Параметры: отсутствуют.

        Возвращаемое значение:
        str: текст с итоговой суммой заказа (например, «Total: $XX.XX»), отображаемый в элементе summary_total_label.
        """
        return self.driver.find_element(*self.total_label).text