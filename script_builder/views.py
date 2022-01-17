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

# from script_builder.helpers import handlezipfile


fs = FileSystemStorage()

# Create your views here.

def thor_logger_view(request):
    # subprocess.Popen('python manage.py bot_init', shell=True)
    # return render(request,'thor_logger.html')
    return render(request,'code_editor.html')


class ScriptBuilderView(APIView):
    def post(self, request):
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

    def get(self, request):
        with open('scripts_folder/print/main.py','rb') as f:
            contents = f.readlines()
            print(contents)

        return Response({
            "code" : contents,
            })
