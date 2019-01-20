from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json

# Create your views here.

def hello(request):
    if request.method == "POST":
        #request = request.get_json(silent = True, force = True)
        print(request.body)
    return (HttpResponse(request))
    #return (JsonResponse({"Hello":"World"}))
