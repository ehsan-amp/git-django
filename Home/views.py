from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def getdata(request):
    return HttpResponse("hhh")
def get1(request,dama,rotobat):
    return HttpResponse(f'dama is {dama} & rotobat is {rotobat}')