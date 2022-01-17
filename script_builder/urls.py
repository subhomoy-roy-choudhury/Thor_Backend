from django.urls import path
from .views import *

urlpatterns = [
    path('thor_logger',thor_logger_view,name = 'thor_logger'),
    path('script_builder/upload',ScriptBuilderView.as_view() ,name = 'script_builder_upload'),
]
