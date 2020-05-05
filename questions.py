import json
import requests

from stackoverflow_service import StackOverFlowService


class Question():

    def __init__(self):
        title = input('Digite a questão: ')
        service = StackOverFlowService(texto=title)
        status, msg = service.status_response()
        if not status:
            print(msg)
        json_response = service.json_response()
        for question in json_response:
            print('Titulo: ', question.get('title'))
            print('Votos: ', question.get('score'))
            print('Link:', question.get('link'), '\n')

Question()
