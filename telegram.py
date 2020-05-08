import telepot
import requests

from stackoverflow_service import StackOverFlowService


class TelegramBot():
    ''' Classe que faz a conexão com bot do telegram.
    '''

    def __init__(self):
        ''' telepot.Bot para poder funcionar precisa do token do gerado via
        BotFather, depois do processo realizado precisa instanciar telepot.Bot
        com o token do Telegram.
        '''
        token_bot = '976260327:AAFDGsVigXLKOGcOjUcc1fW5FhgdMULpSVI'
        self.telegram = telepot.Bot(token_bot)

    def send_msg(self, chat):
        ''' Metodo utilizado para enviar uma mensagem via bot do Telegram.
        '''
        tipo, priv, chat_id = telepot.glance(chat)
        text = chat.get('text')
        print('Mensagem: ', text)
        service = StackOverFlowService(texto=text, tipo=tipo)
        status, msg = service.status_response()
        if not text == '/start':
            if status:
                json_response = service.json_response()
                for question in json_response:
                    text = service.formatted_text(question)
                    self.telegram.sendMessage(chat_id, text)
            else:
                self.telegram.sendMessage(chat_id, msg)

    def received_msg(self):
        '''
        Metodo que capta as informações do telegram.
        - O metodo message_loop vem da instancia Bot da lib telepot, esse metodo
        fica captando as mensagens que entram via telegram, o mesmo pode receber
        uma função que sempre será executada toda vez que entrar uma nova
        informação.
        '''
        return self.telegram.message_loop(self.send_msg)

TelegramBot().received_msg()
while True:
    ''' Processo fica em loop para ficar executando o script.
    '''
    pass
