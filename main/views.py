from django.shortcuts import render
from django.http import HttpResponse
from .models import Settings


# Create your views here.

def SiteSettings(request):

    sitename = Settings.objects.all()

    context = {
        'sitename': sitename
    }

    return render(request, 'frontend/base.html', context)
    # return HttpResponse('<h2>Learn Django</h2>')
