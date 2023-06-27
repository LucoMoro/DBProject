from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def contattaci(request):
    return render(request, 'app/contattaci.html')

def aboutUs(request):
    return render(request, 'app/aboutUs.html')