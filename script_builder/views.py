from django.shortcuts import render
import subprocess
from django.http import JsonResponse
# from .thread import CreateStudentsThread
from rest_framework.views import APIView
from rest_framework.response import Response
import shutil
import zipfile, io
from django.http import HttpResponse, FileResponse
from django.core.files.storage import FileSystemStorage
from glob import glob
import os

# from script_builder.helpers import handlezipfile


fs = FileSystemStorage()

# Create your views here.

def thor_logger_view(request):
    # subprocess.Popen('python manage.py bot_init', shell=True)
    # return render(request,'thor_logger.html')
    return render(request,'script_list.html')

def code_editor_view(request):
    # subprocess.Popen('python manage.py bot_init', shell=True)
    # return render(request,'thor_logger.html')
    return render(request,'code_editor.html')

class ScriptBuilderCodeView(APIView):
    def get(self, request):
        print(request.GET)
        dir_path = request.GET.get('dir_path')
        file_path = request.GET.get('file_path')
        print(dir_path)
        with open(os.path.join(dir_path,file_path),'rb') as f:
            contents = f.readlines()
            print(contents)

        return Response({
            "code" : contents,
            })

class ScriptBuilderView(APIView):
    def post(self, request, task=None):
        print(request.GET, request.FILES)
        zip_file = request.FILES['zip_file']
        print(zip_file.__dict__.items())

        filename_initial = zip_file._name
        script_zip_filename = fs.save(filename_initial, zip_file)


        # script_data = io.BytesIO(zip_file.file)

        z = zipfile.ZipFile(zip_file.file)
        z.extractall("scripts_folder")

        return Response({
            "status" : 1
        }, 200)

    def get(self, request, task=None):
        if task == 'list':
            dir_list = dict()
 
            rootdir = 'scripts_folder'
            for file in os.listdir(rootdir):
                d = os.path.join(rootdir, file)
                if os.path.isdir(d):
                    print(d)
                    # folder_list.append(d)
                    dir_list[d] = os.listdir(d)


            return Response({
                "dir_list": dir_list
                })