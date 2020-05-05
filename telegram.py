import telepot
import requests

from stackoverflow_service import StackOverFlowService


class TelegramBot():

    def __init__(self):
        self.telegram = telepot.Bot('976260327:AAFdQYQDv7ba0kn4W85ztW-bnWyAVxe7O1E')

    def send_msg(self, chat):

        tipo, priv, chat_id = telepot.glance(chat)
        msg = chat.get('text')
        print('msg', msg)
        service = StackOverFlowService(texto=msg, tipo=tipo)
        status, msg = service.status_response()
        if status:
            json_response = service.json_response()
            for question in json_response:
                texto = 'Titulo: {}\nVotos: {}\nLink: {}'.format(
                question.get('title'),
                question.get('score'),
                question.get('link'))
                self.telegram.sendMessage(chat_id, texto)
        else:
            self.telegram.sendMessage(chat_id, msg)

    def received_msg(self):
        return self.telegram.message_loop(self.send_msg)

TelegramBot().received_msg()
while True:
    pass
