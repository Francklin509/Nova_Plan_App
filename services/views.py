from django.shortcuts import render

# Create your views here.
def architechture(request):
    return render(request, 'services/architechture.html')

def conception(request):
    return render(request, 'services/conception.html')

def devis(request):
    return render(request, 'services/devis.html')

def inspection(request):
    return render(request, 'services/inspection.html')

def modern(request):
    return render(request, 'services/modern.html')

def restauration(request):
    return render(request, 'services/restauration.html')

