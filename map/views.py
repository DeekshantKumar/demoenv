from django.shortcuts import render
from django.http import HttpResponse



# def indexView (request):
#     return HttpResponse ("<h1> welcome  </h1>")

# Create your views here.
from django.conf import settings

def map(request):
    key = settings.GOOGLE_API_KEY
    context = {
        'key':key,
    }
    return render(request, 'google/map.html',context)