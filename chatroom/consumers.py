from channels.generic.websocket import AsyncWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer
from index.models import Room, Masseages
from django.contrib.auth.models import User
import json


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = ('chat_%s' % self.room_name).replace('"', '')

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Saving the messages of the user
        f = Masseages()
        f.text = message
        f.room = Room.objects.get(name=(self.room_name).replace('"', ''))
        self.user = self.scope["user"]
        f.sender = User.objects.get(username=self.user.username)
        f.save()

        send = {'text': message, 'username': self.user.username}
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': send

            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))


class loadprevious(WebsocketConsumer):
    def connect(self): # check the user acsess room he not joined (forget)
        self.room_name = self.scope['url_route']['kwargs']['roomName']
        room = Room.objects.filter(name=(self.room_name).replace('"', '')).first()
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
        #print(id)
        room = Room.objects.filter(name=(self.room_name).replace('"', '')).first()
        pervious_masseages = room.masseages.filter(pk__lt=id).order_by('-pk')[:7]

        listofchat = list()
        for item in pervious_masseages:
            pieceofchat = {"user": item.sender.username, "text": item.text, "pk": item.pk}
            listofchat.append(pieceofchat)

        self.send(text_data=json.dumps({"masseages": listofchat}))


class SearchConsumers(WebsocketConsumer):
    def connect(self):
        self.roomName = self.scope['url_route']['kwargs']['roomName']
        self.accept()
    def close(self, code=None):
        pass
    def receive(self, text_data=None, bytes_data=None):

        _data_ = json.loads(text_data)
        first_chars = _data_["firstchars"]
        first_masseage = _data_["firstmasseage"]

        masseages_id=0
        print(first_chars)
        room = Room.objects.filter(name=(self.roomName).replace('"', '')).first()
        try:
            masseages_id = room.masseages.filter(text__icontains=first_chars).order_by('-pk').first().id
            print(masseages_id)
        except:
            self.send(text_data=json.dumps({"masseages_id": 0, "diff": 0}))
            return

        self.send(text_data=json.dumps({"masseages_id": masseages_id, "diff": int(first_masseage)-masseages_id}))
       
