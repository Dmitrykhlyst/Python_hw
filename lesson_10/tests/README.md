📌 Домашнее задание №10
🧪 Автотесты с Allure Report и Page Object Model
📋 Описание
В рамках домашнего задания №10 был реализован автотест интернет-магазина с использованием Selenium WebDriver, pytest, паттерна
Page Object Model (POM) и инструмента отчетности Allure.

🌐 Тестируемый сайт
https://www.saucedemo.com/

🧱 Структура проекта
lesson_10/
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── test_shop.py
│   └── test_calculator.py
│
├── README.md
Что реализовано
🔹 1. Page Object Model

Для каждой страницы сайта создан отдельный класс:

LoginPage — авторизация

InventoryPage — добавление товаров

CartPage — корзина

CheckoutPage — оформление заказа

🔹 2. Автотест интернет-магазина

Тест test_shop_total выполняет следующий сценарий:

Логин под пользователем standard_user

Добавление товаров в корзину

Переход в корзину

Оформление заказа

Заполнение данных покупателя

Проверка итоговой суммы заказа (Total = $58.29)

🔹 3. Интеграция Allure

В тесте использованы:

@allure.title

@allure.description

@allure.feature

@allure.severity

allure.step(...)

Каждый логический шаг теста отображается в Allure-отчёте.

▶️ Запуск тестов

Запуск тестов с генерацией Allure-результатов:

pytest lesson_10/tests/test_shop.py -q --alluredir=allure-results

📊 Просмотр Allure-отчёта
allure serve allure-results


После выполнения команды откроется браузер с подробным HTML-отчётом.