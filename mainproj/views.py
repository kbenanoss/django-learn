from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect 
from home.models import Home
from main.models import Settings

def home(request):
    # return HttpResponse('<h2>Hello Django Lovers</h2>')
    # sitename = "Benanoss Tech | Home"
    site = Settings.objects.get(pk=1)

    sitename = site.title + " | Home"
    # site = Settings.objects.filter(pk=1)
    homedata = Home.objects.all()

    context = {
        'site': site,
        'sitename': sitename,
        'homedata': homedata
    }

    return render(request, 'home.html', context)