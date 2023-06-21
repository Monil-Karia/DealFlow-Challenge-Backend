from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

def home_page(request):
    return HttpResponse("Home page Requested")