from channels.generic.websocket import WebsocketConsumer
from index.models import Room, Masseages
import json

class loadprevious (WebsocketConsumer):

    def connect(self): # check the user acsess room he not joined (forget)

        self.room_name = self.scope['url_route']['kwargs']['roomName']
        room = Room.objects.filter(name=self.room_name).first()
        pervious_masseages = room.masseages.order_by('-pk')[:7] #limiting the masseages to be seven
        # check that the room has no masseages
        if pervious_masseages.first() is None:
            self.accept()
            return

        listofchat = list()
        for item in pervious_masseages:
            pieceofchat = {"user": item.sender.username, "text": item.text, "pk": item.pk}
            listofchat.append(pieceofchat)

        self.accept()
        self.send(text_data=json.dumps({"masseages": listofchat}))




    def close(self, code=None):
        pass

    def receive(self, text_data=None, bytes_data=None):

        data = json.loads(text_data)
        id = data['id']
        room = Room.objects.filter(name=self.room_name).first()
        pervious_masseages = room.masseages.filter(pk__lt=id).order_by('-pk')[:7]

        listofchat = list()
        for item in pervious_masseages:
            pieceofchat = {"user": item.sender.username, "text": item.text, "pk": item.pk}
            listofchat.append(pieceofchat)

        self.send(text_data=json.dumps({"masseages": listofchat}))
