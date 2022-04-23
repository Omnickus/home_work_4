import requests
import json

class HttpRequest:

    """ Класс для HTTP запросов """

    def __new__(cls, *args, **kwargs):
        """
        Разрешается создать объект класса, только в том случае, 
        если будет передан словарь kwargs и значение url будет строкой
        """
        if args:
            return None
        try:
            if kwargs['url'] and type(kwargs['url']) == str:
                return super().__new__(cls)
            else:
                return None
        except Exception as e:
            Exception(f"Ошибка - {e}")
            return None

    def __init__(self, url = None) -> None:
        self.url = url

    @property
    def http_get(self):
        rs = requests.get( self.url ).json()
        return rs

    def http_put(self, id, title, body, userid):
        if self.url != None:
            rs = requests.put( 
                                        url = self.url, 
                                        headers = {'Content-type': 'application/json; charset=UTF-8'}, 
                                        data = json.dumps({ 'id': id, 'title': title, 'body': body, 'userId': userid}))
            return rs.status_code
        else:
            return None
