from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def home(request):
    return JsonResponse({"info": "Django react application", "name": "pruthviraj"})


def next_page(request):
    return JsonResponse({
        "name": "pruthviraj",
        "Tag": "Hello World..!!!"
    })
