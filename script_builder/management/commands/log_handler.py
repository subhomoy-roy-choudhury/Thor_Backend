import logging
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import json
import requests
import sys
from datetime import datetime

class StreamToLogger(object):
    """
    Fake file-like stream object that redirects writes to a logger instance.
    """
    def __init__(self, logger, log_level=logging.INFO):
        self.logger = logger
        self.log_level = log_level
        self.linebuf = ''
        self.channel_layer = get_channel_layer()

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            self.logger.log(self.log_level, line.rstrip())

class RequestsHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        channel_layer = get_channel_layer()
        data = {
            "logs" : json.loads(log_entry)
        }
        print(data)
        async_to_sync(channel_layer.group_send)(
            'new_consumer_group' , {
                'type' : 'thor_logs',
                'value' : json.dumps(data)
            }
        )
        return None

class FormatterLogger(logging.Formatter):
    def __init__(self, task_name=None):
        
        super(FormatterLogger, self).__init__()

    def format(self, record):
        data = dict()
        #['msg', 'filename', 'funcName', 'levelname', 'module','name', 'pathname', 'processName', 'threadName']
        for field,value in record.__dict__.items():
            data[field] = value  
            if field == 'created':
                data['time'] = str(datetime.fromtimestamp(record.created))  

        return json.dumps(data)



def custom_logger(name):
    # logging.basicConfig(
    #    level=logging.DEBUG,
    #    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
    #    # filename="core/management/commands/out.log",
    #    # filemode='a'
    # )

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    custom_handler = RequestsHandler()
    formatter = FormatterLogger(logger)
    custom_handler.setFormatter(formatter)
    logger.addHandler(custom_handler)
    
    return logger

