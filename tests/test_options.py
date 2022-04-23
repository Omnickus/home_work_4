from urllib import request
import pytest
import requests


def test_cmd_options(base_url, cmdopt):
    rs = requests.get(url = base_url)
    assert rs.status_code == int(cmdopt)
