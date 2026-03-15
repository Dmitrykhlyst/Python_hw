import allure
from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        """
        Инициализирует экземпляр страницы инвентаря (товаров).

        Параметры:
        driver: веб‑драйвер Selenium (например, ChromeDriver), используемый для взаимодействия с браузером.
        """
        self.driver = driver
        self.add_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.add_bolt_tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.add_onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("Добавить в корзину рюкзак, футболку Bolt и комбинезон Onesie")
    def add_products(self):
        """
        Добавляет в корзину три конкретных товара: рюкзак Sauce Labs Backpack,
        футболку Sauce Labs Bolt T‑Shirt и комбинезон Sauce Labs Onesie.

        Параметры: отсутствуют.
        Возвращаемое значение: отсутствует.
        """
        self.driver.find_element(*self.add_backpack).click()
        self.driver.find_element(*self.add_bolt_tshirt).click()
        self.driver.find_element(*self.add_onesie).click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        """
        Переходит на страницу корзины, нажимая на ссылку/иконку корзины.

        Параметры: отсутствуют.
        Возвращаемое значение: отсутствует.
        """
        self.driver.find_element(*self.cart_link).click()