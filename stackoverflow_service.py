import requests
import json


class StackOverFlowService():

    def __init__(self, texto, tipo=''):
        self.api_token = 'hV7i0iaQB2CcFEESvPEgDA))'
        self.url = 'https://api.stackexchange.com/2.2/search/'
        self.headers = {'Authorization': self.api_token}
        self.tipo = tipo
        self.params = {
            'site': 'stackoverflow',
            'intitle': texto,
            'order': 'desc',
            'sort': 'votes'}
        self.response = requests.get(
            self.url,
            headers=self.headers,
            params=self.params)

    def status_response(self):
        if self.response.status_code == 200:
            return True, ''
        elif self.tipo in ['document', 'sticker']:
            return False, 'Por favor inserir somente texto!'
        else:
            return False, 'Nenhum resultado encontrado.'

    def json_response(self):
        return self.response.json().get('items')
