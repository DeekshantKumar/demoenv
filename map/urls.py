from django.contrib import admin


from . import views
from .views import *
from django.urls import path, include
from google import views as view


# urlpatterns = [

#     path ('', views.indexView)

# ]

urlpatterns = [
   
   path('map',view.map, name="map"),
   
]