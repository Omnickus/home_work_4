import pytest
from src.class_request import HttpRequest
import re
from config import EXPANSION_IMG, EXPANSION_URL_LINK

@pytest.mark.dogs
@pytest.mark.parametrize("url,status", [
        ("https://dog.ceo/api/breeds/image/random", 'success'),
        ("https://dog.ceo/api/breeds/image/random", 'success'),
        ("https://dog.ceo/api/breeds/image/randomError", 'error'),
        ("https://dog.ceo/api/breeds/image/random", 'success'),
        ("https://dog.ceo/api/breeds/image/random", 'success'),
        ("https://dog.ceo/api/breeds/image/random", 'success'),
    ], ids=['valid_value', 'valid_value', 'valid_value', 'valid_value', 'valid_value', 'valid_value'])
def test_api_status_with_parametrize_dogs(url, status):
    http = HttpRequest(url = url)
    rs = http.http_get['status']
    assert rs == status


@pytest.mark.dogs
@pytest.mark.parametrize("url,code", [
        ("https://dog.ceo/api/breeds/image/randomError", 404),
        ("https://dog.ceo/api/breeds/image/r", 404),
        ("https://dog.ceo/api/bre123WWWWeds/image/random", 404),
    ])
def test_api_code_with_parametrize_dogs(url, code):
    http = HttpRequest(url = url)
    rs = http.http_get['code']
    assert rs == code


@pytest.mark.dogs
def test_api_img_dogs():
    http = HttpRequest(url = 'https://dog.ceo/api/breeds/image/random')
    rs = http.http_get
    assert rs['message'] != ''
    assert rs['status'] != ''


@pytest.mark.dogs
def test_api_expansion_img_dogs():
    http = HttpRequest(url = 'https://dog.ceo/api/breeds/image/random')
    rs = http.http_get['message']
    expansion =  re.findall( r'png$|jpg$|PNG$|JPG$', rs )
    assert expansion[0] in EXPANSION_IMG


@pytest.mark.dogs
def test_api_correct_link_dogs():
    http = HttpRequest(url = 'https://dog.ceo/api/breeds/image/random')
    rs = http.http_get['message']
    correct_link =  re.findall( r'^https:\/\/|^http:\/\/', rs )
    assert correct_link[0] in EXPANSION_URL_LINK
