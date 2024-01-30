from django.urls import path
from . import views


urlpatterns = [
    path('main', views.index, name="home_page")
]
