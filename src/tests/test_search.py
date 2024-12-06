from unittest import TestCase

from fastapi.testclient import TestClient

from main import app  


class TestSearchHandler(TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_search_forms_success_1(self):
        """Переданы все поля 1 целевой формы в запорсе от пользователя"""
        response = self.client.post(
            "/get_form/",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "survey_date": "2024-12-01",
                "feedback_text": "Very satisfied with the product.",
                "respondent_email": "survey.user@example.net",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("Form", response.json())

    def test_search_forms_success_2(self):
        """Переданы все поля 2 целевой формы в запорсе от пользователя"""
        response = self.client.post(
            "/get_form/",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "request_date": "2024-12-01",
                "user_email": "survey.user@example.net",
                "user_phone": "+79291234561"
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("Form", response.json())

    
    def test_search_forms_success_3(self):
        """Переданы все поля целевой формы в запросе от пользователя + несуществующие"""
        response = self.client.post(
            "/get_form/",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "survey_date": "2024-12-01",
                "feedback_text": "Very satisfied with the product.",
                "respondent_email": "survey.user@example.net",
                "some_extra_field": "Wooohooo",
                "some_extra_field2": "Wooohooo2"
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("Form", response.json())

    def test_search_forms_wrong_field(self):
        """Переданы не все поля целевой формы"""
        response = self.client.post(
            "/get_form/",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "feedback_text": "1",
                "respondent_email": "email@example.com",
            },
        )
        print(response.status_code)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.json(),
            {"detail": "Failed find the form by the provided fields"},
        )
    
    def test_search_forms_wrong_field(self):
        """Переданы не все поля целевой + несуществующее"""
        response = self.client.post(
            "/get_form/",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "survey_name": "Example",
                "feedback_text": "1",
                "respondent_email": "email@example.com",
            },
        )
        print(response.status_code)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.json(),
            {"detail": "Failed find the form by the provided fields"},
        )

    def test_search_forms_wrong_field(self):
        """Переданы все поля целевой формы, но тип значения другой"""
        response = self.client.post(
            "/get_form/",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "survey_date": "12-12-1", # неверный формат даты
                "feedback_text": "not validating",
                "respondent_email": "email_example.com", # неверный формат email
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            isinstance(response.json(), str), # Форма есть, но из за несоответсвия типов возвращается не имя, а словарь с типами полей
            False
        )
