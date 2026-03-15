import allure
from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        """
        Инициализирует экземпляр страницы корзины.

        Параметры:
        driver: веб‑драйвер Selenium (например, ChromeDriver), используемый для взаимодействия с браузером.
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    @allure.step("Нажать кнопку оформления заказа (Checkout)")
    def click_checkout(self):
        """
        Нажимает кнопку оформления заказа (Checkout) на странице корзины.

        Параметры: отсутствуют.
        Возвращаемое значение: отсутствует.
        """
        self.driver.find_element(*self.checkout_button).click()