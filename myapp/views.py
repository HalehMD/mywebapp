from django.shortcuts import render
from django.http import HttpResponse
from .models import Order

def write_result(request):

    return HttpResponse("HI")


