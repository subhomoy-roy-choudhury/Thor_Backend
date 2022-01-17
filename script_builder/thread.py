import threading
from asgiref.sync import async_to_sync
import json
import random
from channels.layers import get_channel_layer
import random
import time

# class CreateStudentsThread(threading.Thread):
    
#     def __init__(self):
#         threading.Thread.__init__(self)
        
#     def run(self):
#         try:
#             print('Thread execution started')
#             channel_layer = get_channel_layer()
#             current_total = 0

#             with open("core/management/commands/out.log", "r") as f:
#                 contents = f.readlines()
#                 # print(contents)

#             for content in contents:
#                 data = {
#                     "logs" : content
#                 }
#                 print(data)
#                 async_to_sync(channel_layer.group_send)(
#                     'new_consumer_group' , {
#                         'type' : 'send_notification',
#                         'value' : json.dumps(data)
#                     }
#                 )
#                 #time.sleep(1)
#         except Exception as e:
#             print(e)
#             