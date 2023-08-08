import pytest

from src.report_monaco_2018.flask_report import create_app_flask


class TestFlask:

    """
        Фікстура для створення тестового клієнта Flask.
        Фікстура - створення інкапсульованого середовища, для тестування коду
        В Фікстурі ми створюємо тестового клієнта для тестування коду + HTTP запитів
    """
    @pytest.fixture
    def client(self):

        app = create_app_flask()
        app.testing = True

        return app.test_client()

    # Тест на наявність 'order' та правильний аргумент ?order=desc для всіх сторінок "/report" та "/drivers"
    def test_url_report_order_by_desc(self, client):

        response_report = client.get('/report/?order=desc')

        assert response_report.status_code == 200

        # Отримуємо параметри запиту з відповіді
        query_params_report = response_report.request.args

        assert 'order' in query_params_report

        assert query_params_report['order'] == 'desc'

    def test_url_driver_order_by_desc(self, client):

        response_drivers = client.get('/report/drivers/?order=desc')

        assert response_drivers.status_code == 200

        query_params_drivers = response_drivers.request.args

        assert 'order' in query_params_drivers

        assert query_params_drivers['order'] == 'desc'

    # Тест на неправильний агрумент 'order' => ?order=f4d5f4d5
    def test_report_order_with_invalid_value(self, client):

        # Виконуємо HTTP-запит з неправильним значенням параметра 'order'
        response_report = client.get('/report/', query_string={'order': 'invalid_value'})

        # Перевіряємо, чи відповідь має статус 400
        assert response_report.status_code == 400

    def test_driver_order_with_invalid_value(self, client):

        response_drivers = client.get('/report/drivers/', query_string={'order': 'invalid_value'})
        assert response_drivers.status_code == 400

