from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render 
from django.http import HttpResponse

    

def index(request):
    return HttpResponse("hola")
