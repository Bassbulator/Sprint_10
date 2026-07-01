import allure
import pytest

from test_data import TestData

TARIFF_HINT_CASES = [
    ("Рабочий", "verify_business_tariff_hint"),
    ("Отпускной", "verify_holiday_tariff_hint"),
    ("Уютный", "verify_cozy_tariff_hint"),
    ("Гламурный", "verify_glamour_tariff_hint"),
    pytest.param(
        "Разговорчивый",
        "verify_chatty_tariff_hint",
        marks=pytest.mark.xfail(
            reason="Известный дефект: описание тарифа «Разговорчивый» не совпадает с ожидаемым"
        ),
    ),
    pytest.param(
        "Сонный",
        "verify_sleepy_tariff_hint",
        marks=pytest.mark.xfail(
            reason="Известный дефект: описание тарифа «Сонный» не совпадает с ожидаемым"
        ),
    ),
]

ORDER_FORM_FIELD_CASES = [
    ("комментария", "comment_field_visible"),
    ("телефона", "phone_field_visible"),
    ("оплаты", "payment_field_visible"),
    ("требований", "requirements_visible"),
]


class TestOrderFlow:

    @allure.title("Блок выбора тарифа появляется после нажатия «Вызвать такси»")
    @allure.description(
        "Проверяет, что после нажатия на кнопку вызова такси открывается блок с тарифами "
        "и один из них оказывается выбранным по умолчанию"
    )
    def test_tariff_block_shown_and_default_tariff_selected(self, tariff_screen_ready):
        with allure.step("Убедиться, что один из тарифов выбран"):
            assert tariff_screen_ready.any_tariff_selected()

    @allure.title("На экране тарифов отображается поле {field_name}")
    @allure.description(
        "Проверяет наличие отдельного поля формы заказа после перехода к выбору тарифа"
    )
    @pytest.mark.parametrize("field_name, check_method", ORDER_FORM_FIELD_CASES)
    def test_tariff_order_form_field_visible(
        self, tariff_screen_ready, field_name, check_method
    ):
        with allure.step(f"Проверить наличие поля {field_name}"):
            assert getattr(tariff_screen_ready, check_method)()

    @allure.title("Подсказка тарифа «{tariff_name}» соответствует ожидаемому описанию")
    @allure.description(
        "Проверяет, что при наведении на кнопку информации у тарифа "
        "отображается верный текст подсказки"
    )
    @pytest.mark.parametrize("tariff_name, verify_method", TARIFF_HINT_CASES)
    def test_tariff_hint_matches_expected_description(
        self, tariff_screen_ready, tariff_name, verify_method
    ):
        with allure.step(f"Проверить подсказку тарифа «{tariff_name}»"):
            assert getattr(tariff_screen_ready, verify_method)()

    @allure.title("Окно поиска машины отображает ожидаемый заголовок")
    @allure.description(
        "Проверяет заголовок окна после оформления заказа с тарифом «Рабочий»"
    )
    def test_searching_taxi_window_shows_expected_title(self, order_placed):
        with allure.step("Проверить заголовок окна поиска"):
            assert (
                order_placed["searching"].get_window_title()
                == TestData.SEARCHING_TAXI_TITLE
            )

    @allure.title("Окно поиска машины содержит кнопку отмены")
    @allure.description(
        "Проверяет наличие кнопки отмены в окне поиска после оформления заказа"
    )
    def test_searching_taxi_window_shows_dismiss_button(self, order_placed):
        with allure.step("Проверить наличие кнопки отмены"):
            assert order_placed["searching"].dismiss_btn_visible()

    @allure.title("Окно поиска машины содержит таймер обратного отсчёта")
    @allure.description(
        "Проверяет наличие таймера в окне поиска после оформления заказа"
    )
    def test_searching_taxi_window_shows_countdown(self, order_placed):
        with allure.step("Проверить наличие таймера обратного отсчёта"):
            assert order_placed["searching"].countdown_visible()

    @allure.title("Окно активной поездки отображает ожидаемый заголовок")
    @allure.description(
        "Проверяет заголовок окна после завершения поиска машины"
    )
    def test_active_ride_window_shows_expected_title(self, active_ride_screen):
        with allure.step("Проверить заголовок окна активной поездки"):
            assert TestData.CAR_ARRIVING_TITLE in active_ride_screen["ride"].get_title()

    @allure.title("Окно активной поездки отображает номер автомобиля")
    @allure.description(
        "Проверяет наличие номера автомобиля после завершения поиска машины"
    )
    def test_active_ride_window_shows_license_plate(self, active_ride_screen):
        with allure.step("Проверить наличие номера автомобиля"):
            assert active_ride_screen["ride"].license_plate_visible()

    @allure.title("Окно активной поездки отображает изображение автомобиля")
    @allure.description(
        "Проверяет наличие изображения автомобиля после завершения поиска машины"
    )
    def test_active_ride_window_shows_vehicle_image(self, active_ride_screen):
        with allure.step("Проверить наличие изображения автомобиля"):
            assert active_ride_screen["ride"].vehicle_image_visible()

    @allure.title("Окно активной поездки отображает фото водителя")
    @allure.description(
        "Проверяет наличие фото водителя после завершения поиска машины"
    )
    def test_active_ride_window_shows_driver_photo(self, active_ride_screen):
        with allure.step("Проверить наличие фото водителя"):
            assert active_ride_screen["ride"].driver_photo_visible()

    @allure.title("Окно активной поездки отображает имя водителя")
    @allure.description(
        "Проверяет наличие имени водителя после завершения поиска машины"
    )
    def test_active_ride_window_shows_driver_name(self, active_ride_screen):
        with allure.step("Проверить наличие имени водителя"):
            assert active_ride_screen["ride"].driver_name_visible()

    @allure.title("Окно активной поездки отображает рейтинг водителя")
    @allure.description(
        "Проверяет наличие рейтинга водителя после завершения поиска машины"
    )
    def test_active_ride_window_shows_driver_score(self, active_ride_screen):
        with allure.step("Проверить наличие рейтинга водителя"):
            assert active_ride_screen["ride"].driver_score_visible()

    @allure.title("Окно активной поездки содержит кнопку отмены")
    @allure.description(
        "Проверяет наличие кнопки отмены после завершения поиска машины"
    )
    def test_active_ride_window_shows_dismiss_button(self, active_ride_screen):
        with allure.step("Проверить наличие кнопки отмены"):
            assert active_ride_screen["ride"].dismiss_btn_visible()

    @allure.title("Окно активной поездки содержит кнопку информации")
    @allure.description(
        "Проверяет наличие кнопки информации после завершения поиска машины"
    )
    def test_active_ride_window_shows_info_button(self, active_ride_screen):
        with allure.step("Проверить наличие кнопки информации"):
            assert active_ride_screen["ride"].info_btn_visible()

    @allure.title("Стоимость в деталях поездки совпадает с выбранным тарифом")
    @allure.description(
        "Проверяет, что цена в деталях поездки соответствует стоимости тарифа «Рабочий»"
    )
    def test_ride_details_price_matches_business_tariff(self, order_placed_with_price):
        searching = order_placed_with_price["searching"]
        ride = order_placed_with_price["ride"]
        details = order_placed_with_price["details"]

        with allure.step("Дождаться завершения поиска машины"):
            searching.wait_search_complete()

        with allure.step("Открыть детали поездки"):
            ride.open_details()
            details.await_pickup_address()

        with allure.step("Сравнить стоимость тарифа и деталей поездки"):
            tariff_price = order_placed_with_price["price"][0].replace(" ", "")
            details_price = details.get_fare_text().replace(" ", "")
            assert tariff_price in details_price

    @allure.title("Отмена поездки закрывает панель активной поездки")
    @allure.description(
        "Проверяет, что после нажатия «Отменить» панель активной поездки скрывается"
    )
    def test_cancel_ride_closes_active_ride_panel(self, active_ride_screen):
        ride = active_ride_screen["ride"]

        with allure.step("Отменить поездку"):
            ride.dismiss()

        with allure.step("Дождаться закрытия панели активной поездки"):
            ride.wait_panel_closed()
