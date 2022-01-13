from channels.generic.websocket import WebsocketConsumer

class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.accept("subprotocol")
        self.close()

    def receive(self, text_data=None, bytes_data=None):
        self.send(text_data="Hello world!")
        self.send(bytes_data="Hello world!")
        self.close()
        self.close(code=4123)

    def disconnect(self, close_code):
        # Called when the socket closes
        pass