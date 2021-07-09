from django.shortcuts import render
from django.http import HttpResponse


def advertisements_list(request, *args, **kwargs):
    return render(request, "advertisements/advertisements_list.html", {})

def advertisements_detail (request):
    return HttpResponse("<h2>О сайте</h2>")

def advertisements_data_scientist (request, *args, **kwargs):
    return render(request, "advertisements/data-scientist/data_scientist.html", {})

def advertisements_java_job (request, *args, **kwargs):
    return render(request, "advertisements/java-job/java_job.html", {})

def advertisements_python_job (request, *args, **kwargs):
    return render(request, "advertisements/python-job/python_job.html", {})

def advertisements_test_job (request, *args, **kwargs):
    return render(request, "advertisements/test-job/test_job.html", {})

def advertisements_web_job (request, *args, **kwargs):
    return render(request, "advertisements/web-job/web_job.html", {})




# Create your views here.
