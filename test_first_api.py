import requests


class TestFirstApi:
    def test_hello_call(self):
        url = "https://playground.learnqa.ru/api/hello"
        name = "Mike"
        data = {'name': name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, "Wrong response code"

        response_dict = response.json()
        assert "answer" in response_dict, "Не найден 'answer'в ответе"

        expected_response_text = f"Hello, {name}"
        actual_response_text = response_dict["answer"]
        assert actual_response_text == expected_response_text, "Актуальный текст отличается от ожидаемого результата"
