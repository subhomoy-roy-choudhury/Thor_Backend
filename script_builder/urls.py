from django.urls import path
from .views import *

urlpatterns = [
    path('thor_logger',thor_logger_view,name = 'thor_logger'),
    path('script_builder/upload/<str:task>/',ScriptBuilderView.as_view() ,name = 'script_builder_upload'),
    path('script_builder/code/editor/',ScriptBuilderCodeView.as_view() ,name = 'script_builder_code'),
    path('scripts/',code_editor_view ,name = 'code_editor'),
]
