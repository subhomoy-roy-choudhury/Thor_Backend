from django.urls import path
from .views import *

urlpatterns = [
    path('thor_logger',thor_logger_view,name = 'thor_logger'),
    path('script_builder/upload/<str:task>/',ScriptBuilderView.as_view() ,name = 'script_builder_upload'),
    path('script_builder/add/<str:file_type>/',AddContent.as_view() ,name = 'script_builder_add'),
    path('script_builder/delete/<str:file_type>/',DeleteContent.as_view() ,name = 'script_builder_delete'),
    path('script_builder/code/editor/',ScriptBuilderCodeView.as_view() ,name = 'script_builder_code_editor'),
    path('script_builder/code/test/',TestCaseCheckView.as_view() ,name = 'script_builder_code_test'),
    path('script_builder/code/save/',SaveCodeView.as_view() ,name = 'script_builder_code_save'),
    path('scripts/',code_editor_view ,name = 'code_editor'),
]
