from django.shortcuts import render

# Create your views here.

def Site_settings(request):
    
    return render(request, 'frontend/index.html')

def index(request):
    return render(request, 'frontend/index.html')
