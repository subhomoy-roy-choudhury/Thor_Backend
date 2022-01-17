from channels.generic.websocket import WebsocketConsumer, AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync
import json

class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "test_customer"
        self.room_group_name = "test_customer_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_name, self.room_group_name
        )
        self.accept()
        self.send(text_data=json.dumps({"status":"connected"}))

    def receive(self, text_data=None, bytes_data=None):
        print(text_data)
        self.send(text_data=json.dumps({'status' : 'we got you'}))

    def disconnect(self, close_code):
        print('disconnected')


class NewConsumer(AsyncJsonWebsocketConsumer):
    
    async def connect(self):
        self.room_name = 'new_consumer'
        self.room_group_name = "new_consumer_group"
        
        await(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
        # self.user = self.scope["user"]
        # print(self.user)
        await self.send(text_data=json.dumps({'status' : 'connected from new async json consumer'}))
        # CreateStudentsThread().start()
        
        
    async def receive(self, text_data):
        print(text_data)
        await self.send(text_data=json.dumps({'status' : 'we got you'}))


    async def disconnect(self , *args, **kwargs):
        await print('disconnected')
    
    async  def send_notification(self , event):
        data = json.loads(event.get('value'))
        await self.send(text_data=json.dumps({'payload' : data}))

    async  def thor_logs(self , event):
        data = json.loads(event.get('value'))
        await self.send(text_data=json.dumps({'payload' : data}))