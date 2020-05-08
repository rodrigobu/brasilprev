import json
import requests

from stackoverflow_service import StackOverFlowService


class SearchStackOverFlow():
    '''Classe que recebe um input via terminal e retorna a pesquisa que a partir
    das informações do input.
    '''

    def __init__(self):
        title = input('Faça sua pesquisa: ')
        service = StackOverFlowService(texto=title)
        status, msg = service.status_response()
        if not status:
            print(msg)
        json_response = service.json_response()
        for question in json_response:
            text = service.formatted_text(question)
            print(text)

SearchStackOverFlow()
