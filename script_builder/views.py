from this import d
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
import json
import importlib.util
import unittest
from .helpers import TextTestResultWithSuccesses
from .constants import code_main, code_test

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

class TestCaseCheckView(APIView):
    def post(self,request):
        dir_path = request.data.get('dir_path')
        print(dir_path)

        '''
        Refer https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
        '''

        spec = importlib.util.spec_from_file_location("TestSequenceFunctions",os.path.join(f"{dir_path}","test.py") )
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
        # TestSequenceFunctions

        '''
        Refer https://stackoverflow.com/questions/40613177/how-to-loop-over-all-success-test-results-of-a-python-unittest-runner
        '''

        test_obj = foo.TestSequenceFunctions
        suite = unittest.TestLoader().loadTestsFromTestCase(test_obj)
        testResult = unittest.TextTestRunner(verbosity=2,resultclass=TextTestResultWithSuccesses).run(suite)
        # print(testResult.__dict__.items())
        # print(testResult.errors[0][0].__dict__.items())

        results = dict()
        if len(testResult.failures) > 0 : 
            results['failure'] = list()
            for t in testResult.failures:
                # print(t[0].id())
                # print(t[1])
                failure_item = {
                    "id" : t[0].id(),
                    "trackback" : t[1]
                }
                results['failure'].append(failure_item)

        if len(testResult.errors) > 0 :
            results['error'] = list() 
            for t in testResult.errors:
                # print(t[0].id())
                # print(t[1])
                error_item = {
                    "id" : t[0].id(),
                    "trackback" : t[1]
                }
                results['error'].append(error_item)

        if len(testResult.successes) > 0  :
            results['success'] = list() 
            for t in testResult.successes:
                print(t.id())
                success_item = {
                    "id" : t.id(),
                }
                results['success'].append(success_item)

        return Response({
            "tests": results
        })

class SaveCodeView(APIView):
    def post(self,request):
        print(request.data)
        dir_path = request.data.get('dir_path')
        file_path = request.data.get('file_path')
        code = request.data.get('code')
        print(dir_path)
        with open(os.path.join(dir_path,file_path), "w") as f:
            # contents = "".join(contents)
            f.write(code)
        return Response({
            "status": 1
        })


class AddContent(APIView):
    def post(self,request,file_type=None):
        if file_type == 'folder':
            folder_name = request.data.get('folder_name')
            folder_path = os.path.join('scripts_folder',folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

                # Create __init__.py

                file_path = os.path.join(folder_path,'__init__.py')
                f = open(file_path, 'w')  # open file in write mode
                f.write('# Written By Thor AI Script Builder')
                f.close()

                # Create main.py
                
                file_path = os.path.join(folder_path,'main.py')
                f = open(file_path, 'w')  # open file in write mode
                f.write(code_main)
                f.close()

                # Create test.py

                file_path = os.path.join(folder_path,'test.py')
                f = open(file_path, 'w')  # open file in write mode
                f.write(code_test)
                f.close()

                # Create requirements.txt

                file_path = os.path.join(folder_path,'requirements.txt')
                f = open(file_path, 'w')  # open file in write mode
                f.write('# Written By Thor AI Script Builder')
                f.close()

                return Response({
                    "satus": 1,
                    "data": "Created Successfully"
                })
            return Response({
                "status": 0,
                "data" : "folder already exists"
            })
        elif file_type == "file":
            file_name = request.data.get('file_name')
            dir_path = request.data.get('dir_path')
            file_path = os.path.join(dir_path,file_name)
            if not os.path.exists(file_path):
                f = open(file_path, 'w')  # open file in write mode
                f.write('# Written By Thor AI Script Builder')
                f.close()
                return Response({
                    "satus": 1,
                    "data": "Created Successfully"
                })
            return Response({
                "status": 0,
                "data" : "file already exists"
            })
