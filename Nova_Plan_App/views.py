#from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("Hello World")
    return render(request, 'homepage.html')


def about(request):
    # return HttpResponse("Hi this is my about page")
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def team(request):
    return render(request, 'team.html')

def service(request):
    return render(request, 'service.html')