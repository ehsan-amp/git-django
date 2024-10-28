from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    from Home.models import TblData
    new1=TblData.objects.all()[2]
    return HttpResponse(f"Temperature = {new1.temperature}, Humidity = {new1.humidity}")
def getdata(request):
    return render(request,'Home/Data-list.html')
def get1(request,dama,rotobat):
    from Home.models import TblData
    new_data = TblData(temperature=dama, humidity=rotobat)
    new_data.save()
    return HttpResponse(f'dama is {dama} & rotobat is {rotobat}')