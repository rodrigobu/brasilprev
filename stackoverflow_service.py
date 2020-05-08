import requests
import json


class StackOverFlowService():
    ''' Classe que faz a conexão com api e validações do
    Stack Overflow
    '''
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
        ''' Metodo que valida o retorno da api e do tipo do conteudo
        que está sendo enviado para api.
        Essa validação evita quando utilizado o bot do telegram para ele barrar
        tipo de conteudo for document ou sticker
        '''

        if self.response.status_code == 200:
            return True, ''
        elif self.tipo in ['document', 'sticker']:
            return False, 'Por favor inserir somente texto!'
        else:
            return False, 'Nenhum resultado encontrado.'

    def json_response(self):
        ''' Metodo que retorna o json do do stack overflow
        '''
        return self.response.json().get('items')

    def formatted_text(self, item):
        text = 'Titulo: {}\nVotos: {}\nLink: {}\n'.format(
        item.get('title'),
        item.get('score'),
        item.get('link'))
        return text
