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