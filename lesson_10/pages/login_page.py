import allure
from selenium.webdriver.common.by import By

class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        """
        Инициализирует экземпляр страницы авторизации.

        Параметры:
        driver: веб‑драйвер Selenium (например, ChromeDriver), используемый для взаимодействия с браузером.
        """
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    @allure.step("Открыть страницу авторизации")
    def open(self):
        """
        Открывает страницу авторизации по указанному URL.

        Параметры: отсутствуют.
        Возвращаемое значение: отсутствует.
        """
        self.driver.get(self.URL)

    @allure.step("Ввести имя пользователя: {username}")
    def enter_username(self, username: str):
        """
        Вводит имя пользователя в соответствующее поле на странице авторизации.

        Параметры:
        username (str): имя пользователя для авторизации, которое будет введено в поле «User Name».

        Возвращаемое значение: отсутствует.
        """
        self.driver.find_element(*self.username_input).send_keys(username)

    @allure.step("Ввести пароль: {password}")
    def enter_password(self, password: str):
        """
        Вводит пароль в соответствующее поле на странице авторизации.

        Параметры:
        password (str): пароль пользователя для авторизации, который будет введён в поле «Password».

        Возвращаемое значение: отсутствует.
        """
        self.driver.find_element(*self.password_input).send_keys(password)

    @allure.step("Нажать кнопку входа (Login)")
    def click_login(self):
        """
        Нажимает кнопку входа (Login) для отправки формы авторизации и перехода в систему.

        Параметры: отсутствуют.
        Возвращаемое значение: отсутствует.
        """
        self.driver.find_element(*self.login_button).click()