from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

# from django.Thor_Backend import Thor_Backend
import time

class Command(BaseCommand):
    help = 'Create Indices for Elastic Search'

    def add_arguments(self, parser):
        # parser.add_argument('model_name', type=str, help='Name of the Elastic Search model')
        # parser.add_argument('-a', '--app_name', type=str, help='Name of the Django APP', )
        pass

    def handle(self, *args, **kwargs):
        # model_name = kwargs['model_name']
        # app_name = kwargs['app_name']
        i= 0
        while True:
            print(i)
            time.sleep(3)
            i+=1
        
        # app_models = apps.get_app_config(app_name).get_models()
        # app_models_namelist = [name._meta.object_name for name in app_models]
        # if model_name in app_models_namelist:
        #     elastic_search_instance = ElasticSearchMaster(model_name)
        #     response_data = elastic_search_instance.opensearch_createdbindex()
        #     self.stdout.write(self.style.SUCCESS('Index Created Successfully for %s (%s) !' % (model_name, app_name)))
        #     # print(model_name._meta.object_name,model_name._meta.app_label)
        # else :
        #     self.stdout.write(self.style.WARNING('Model Does Not Exist'))
