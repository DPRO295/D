from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer

class ChatConsumer(WebsocketConsumer):

    def websocket_connect(self, message):
        print("*** Connection Accept *** ")
        self.accept()

    def websocket_receive(self, message):
        print("Received message:", message)
        self.send(text_data='OK')

    def websocket_disconnect(self, message):
        print("*** Connection Closing ***")
        raise StopConsumer()

import json

class MyConsumer(WebsocketConsumer):

    def New_Watch_number(self, event):
        # print(event)
        self.send(text_data=json.dumps({
            "type": "New_Watch_number",
            "reward_id": event["reward_id"],
            "watches": event["watches"]
        }))
    def New_Answer(self, event):
        self.send(text_data=json.dumps(event))
    def New_Accept_Reward(self, event):
        self.send(text_data=json.dumps(event))
    def New_Like_number(self, event):
        self.send(text_data=json.dumps(event))

    def New_Tip(self, event):
        self.send(text_data=json.dumps(event))

    def NewData(self, event):
        print(event)
        self.send(text_data=json.dumps({
            "type": "error",
            "message": "Invalid message type: %s" % event["type"]
        }))

    def connect(self):
        self.accept()
        async_to_sync(self.channel_layer.group_add)(
            "my_group",
            self.channel_name
        )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            "my_group",
            self.channel_name
        )

    def receive(self, text_data):
        message = json.loads(text_data)
        if message["type"] == "show_alert":
            # show a popup alert in web page
            self.send(text_data=json.dumps({
                "type": "show_alert",
                "message": message["message"]
            }))
        elif message["type"] == "error":
            # handle "error" message
            self.handle_error(message)
        elif message["type"] == "NewData":
            print("GAGA")
        else:
            # send an error message to client
            self.send(text_data=json.dumps({
                "type": "error",
                "message": "Invalid message type: %s" % message["type"]
            }))
