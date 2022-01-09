import pytest
import requests


@pytest.fixture()
def setup():
    api_url = "https://eacp.energyaustralia.com.au/codingtest/api/v1/festivals"
    response = requests.get(api_url)
    return response

