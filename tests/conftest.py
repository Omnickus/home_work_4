import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--url", 
        default = "https://ya.ru", 
        help = "write the url"
    )
    parser.addoption(
        "--status_code", 
        default = 200,
        help = "write status code"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")

@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--status_code")
