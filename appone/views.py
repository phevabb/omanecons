from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def service(request):
    return render(request, 'service.html')


def contact(request):
    return render(request, 'contact.html')


def project(request):
    return render(request, 'project.html')

def logistics(request):
    return render(request, 'logistic.html')

def engine(request):
    return render(request, 'engine.html')

def handyman(request):
    return render(request, 'handyman.html')


def index2(request):
    return render(request, 'index2.html')