from channels.generic.websocket import WebsocketConsumer

import json

class loadprevious (WebsocketConsumer):

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['roomName']
        print(self.room_name)
        self.accept()


    def close(self, code=None):
        pass

    def receive(self, text_data=None, bytes_data=None):

        pass