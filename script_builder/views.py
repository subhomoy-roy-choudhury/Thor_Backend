from django.shortcuts import render
import subprocess


# Create your views here.

def home(request):
    # subprocess.Popen('python manage.py bot_init', shell=True)
    return render(request)