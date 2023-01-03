from django.shortcuts import render
from django.http import HttpResponse

def geehome (request):
    # return render(request, 'index.html')
    return HttpResponse ("<h1> hi </h1>")