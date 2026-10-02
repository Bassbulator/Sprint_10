# Sprint_10 — Автотесты для Яндекс.Маршруты

## Стек

- **Python** 3.x
- **Selenium** — UI-автоматизация
- **pytest** — тест-фреймворк
- **Allure** — генерация отчётов
- **Page Object Model** — архитектурный паттерн

## Структура проекта

```
Sprint_10/
├── locators/               # CSS/XPath локаторы элементов
│   ├── common_locators.py
│   ├── address_form_locators.py
│   ├── transport_picker_locators.py
│   ├── tariff_selection_locators.py
│   ├── searching_taxi_locators.py
│   ├── active_ride_locators.py
│   └── ride_details_locators.py
├── pages/                  # Page Object классы
│   ├── base_page.py
│   ├── address_form.py
│   ├── transport_picker.py
│   ├── tariff_selector.py
│   ├── searching_taxi.py
│   ├── active_ride.py
│   └── ride_details.py
├── tests/                  # Тестовые модули
│   ├── test_route_display.py
│   ├── test_route_panel.py
│   ├── test_mode_switching.py
│   └── test_order_flow.py
├── conftest.py             # pytest-фикстуры
├── constants.py            # URL приложения
├── test_data.py            # Тестовые данные
└── helpers.py              # Фабрика браузеров
```

## Установка зависимостей

```bash
pip install -r requirements.txt
```

## Запуск тестов

```bash
pytest -v
```

## Запуск с генерацией Allure-отчёта

```bash
pytest tests/ --alluredir=allure_results
allure serve allure_results
```
