import pytest
from src.class_request import HttpRequest
import re
from config import EXPANSION_URL_LINK


@pytest.mark.openbrewerydb
@pytest.mark.parametrize("url,name", [
        ("https://api.openbrewerydb.org/breweries?by_name=", 'Flying%20Bike%20Cooperative%20Brewery'),
        ("https://api.openbrewerydb.org/breweries?by_name=", 'Utah%20Brewers%20Cooperative'),
        ("https://api.openbrewerydb.org/breweries?by_name=", 'Cooper%20Landing%20Brewing%20Company'),
    ], ids=['valid_value', 'valid_value', 'valid_value'])
def test_openbrewerydb_get_by_name(url, name):
    http = HttpRequest(url = url + name)
    rs = http.http_get
    correct_link = re.findall( r'^https:\/\/|^http:\/\/', rs[0]['website_url'] )
    assert correct_link[0] in EXPANSION_URL_LINK


@pytest.mark.openbrewerydb
@pytest.mark.parametrize("url,param", [
        ("https://api.openbrewerydb.org/breweries/search?query=", 'Center Pivot'),
        ("https://api.openbrewerydb.org/breweries/search?query=", 'Cape Ann Lanes'),
        ("https://api.openbrewerydb.org/breweries/search?query=", 'Camino Brewing Co LLC'),
    ])
@pytest.mark.openbrewerydb
def test_openbrewerydb_search_full_str(url, param):
    http = HttpRequest(url = url + param)
    rs = http.http_get
    for i in rs:
        param = str(param).upper()
        string = str(i['name']).upper()
        result = re.findall( fr'{param}', string)
        assert len(result) != 0


@pytest.mark.openbrewerydb
def test_openbrewerydb_id_str():
    http = HttpRequest(url = 'https://api.openbrewerydb.org/breweries')
    rs = http.http_get
    for i in rs:
        assert type(i['id']) == str
        assert type(i['name']) == str


@pytest.mark.openbrewerydb
def test_openbrewerydb_search_short_str():
    http = HttpRequest(url = "https://api.openbrewerydb.org/breweries/autocomplete?query=dog")
    rs = http.http_get
    for i in rs:
        assert len(i) == 2

        
@pytest.mark.openbrewerydb
def test_openbrewerydb_search_by_state():
    http = HttpRequest(url = "https://api.openbrewerydb.org/breweries?by_state=new_york")
    rs = http.http_get
    for i in rs:
        assert i['state'] != ''
