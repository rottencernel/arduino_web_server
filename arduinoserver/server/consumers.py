import json
from channels.generic.websocket import WebsocketConsumer


class ArduinoConsumer(WebsocketConsumer):
    def connect(self):
        self.signal = self.scope['url_route']['kwargs']
        self.signal_name = '%s' % self.signal

        self.channel_layer.group_add(
            self.signal_name,
            self.channel_name
        )

        self.accept()

        self.channel_layer.group_send(
            self.signal_name,
            {
                'type': 'tester_message',
                'message': 'hello'
            }
        )

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        if 'Hello' in text_data:
            print('its ok')
        # self.send()
        pass