import pytest
import requests

class TestParametrizeApi:
    names = [("Mike"), ("Margo"), ("")]

    @pytest.mark.parametrize('name',names)
    def test_hello_call(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {'name':name}


        response = requests.get(url,params=data)

        assert response.status_code == 200, "Wrong response"


        response_dict = response.json()

        assert "answer" in response_dict, "отсутствует поле 'answer' в ответе"
        if len(name) == 0:
            expected_response_text = "Hello, someone"
        else:

            expected_response_text = f"Hello, {name}"

        actual_response_text = response_dict["answer"]
        assert actual_response_text == expected_response_text, "Актуальный текст в ответе не корректен"
