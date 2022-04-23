import pytest
from src.class_request import HttpRequest
import re
from config import EXPANSION_URL_LINK



@pytest.mark.jsonplaceholder
@pytest.mark.parametrize("url,id,comments", [
        ("https://jsonplaceholder.typicode.com/posts/", 1, '/comments'),
        ("https://jsonplaceholder.typicode.com/posts/", 2, '/comments'),
        ("https://jsonplaceholder.typicode.com/posts/", 3, '/comments'),
    ], ids=['valid_value', 'valid_value', 'valid_value'])
def test_jsonplaceholder_comments(url, id, comments):
    http = HttpRequest(url = url + str(id) + comments )
    rs = http.http_get
    for i in rs:
        assert i['body'] != ''
        assert len(re.findall( fr'^.+@.+\..+$', i['email'] )) == 1


@pytest.mark.jsonplaceholder
def test_jsonplaceholder_correct_post_type():
    http = HttpRequest(url = 'https://jsonplaceholder.typicode.com/posts')
    rs = http.http_get
    for i in rs:
        assert type(i['userId']) == int
        assert type(i['id']) == int
        assert type(i['title']) == str
        assert type(i['body']) == str


@pytest.mark.jsonplaceholder
def test_jsonplaceholder_correct_photo_link():
    http = HttpRequest(url = 'https://jsonplaceholder.typicode.com/photos')
    rs = http.http_get
    for i in rs:
        correct_link_url = re.findall( r'^https:\/\/|^http:\/\/', i['url'] )
        correct_link_thumbnailUrl = re.findall( r'^https:\/\/|^http:\/\/', i['url'] )
        assert correct_link_url[0] in EXPANSION_URL_LINK
        assert correct_link_thumbnailUrl[0] in EXPANSION_URL_LINK


@pytest.mark.jsonplaceholder
def test_jsonplaceholder_get_users():
    http = HttpRequest(url = 'https://jsonplaceholder.typicode.com/users')
    rs = http.http_get
    for i in rs:
        assert type(i['id']) == int
        assert type(i['name']) == str
        assert type(i['email']) == str
        assert len(re.findall( fr'^.+@.+\..+$', str(i['email']) )) == 1


@pytest.mark.jsonplaceholder
def test_jsonplaceholder_put_comment():
    http = HttpRequest(url = 'https://jsonplaceholder.typicode.com/posts/1')
    rs = http.http_put(id = 101, title = 'TEST1', body = 'BODY TO TEST1', userid = 1)
    assert rs == 200
