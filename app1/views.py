from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first_app1(request):
    return HttpResponse('This is app1 page')