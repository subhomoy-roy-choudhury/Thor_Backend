import logging
import sys
import time
import multiprocessing
import json

# from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

import random
import threading

from .log_handler import custom_logger, StreamToLogger
from .main_app import main as thor_main

class Processes:
    @staticmethod
    def debug_logs_write(*args, **kwargs):
        # # stdout_logger = logging.getLogger('STDOUT')
        # stdout_logger = custom_logger('STDOUT')

        # # custom_handler = RequestsHandler()
        # # stdout_logger.addHandler(custom_handler)
        # sl = StreamToLogger(stdout_logger, logging.INFO)
        # sys.stdout = sl
        
        # # stderr_logger = logging.getLogger('STDERR') 
        # stderr_logger = custom_logger('STDERR') 
        # # stderr_logger.addHandler(custom_handler)
        # sl = StreamToLogger(stderr_logger, logging.ERROR)
        # sys.stderr = sl
        logger = custom_logger("thor_backend")
        logger.exception("{'sample json message' : '2'}")
        thor_main(logger)

        # logger = custom_logger("thor_backend")
        # logger.exception("{'sample json message' : '2'}")

        # print("Test to standard out")
        # for i in range(5):
        #     logger.debug("Harmless debug Message")
        #     logger.info("Just an information")
        #     logger.warning("Its a Warning")
        #     logger.error("Did you try to divide by zero")
        #     logger.critical("Internet is down")
        #     time.sleep(1)
        # logger.exception('Test to standard error')


class Command(BaseCommand):
    help = 'Create Indices for Elastic Search'

    def add_arguments(self, parser):
        # parser.add_argument('model_name', type=str, help='Name of the Elastic Search model')
        # parser.add_argument('-a', '--app_name', type=str, help='Name of the Django APP', )
        pass

    def handle(self, *args, **kwargs):
        # model_name = kwargs['model_name']
        # app_name = kwargs['app_name']

        Processes.debug_logs_write()
                
