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
