from django.shortcuts import render

# Create your views here.
def registration(request):
    return render(request, 'users/registration.html')

def login(request):
    return render(request, 'users/login.html')

def profile_management(request):
    return render(request, 'users/profile.html')

def payment(request):
    return render(request, 'users/payment.html')

