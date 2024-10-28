from os import times

from django.shortcuts import render
from django.http import HttpResponse
from Home.models import TblData
from datetime import datetime
# Create your views here.
def home(request):
    #from Home.models import TblData
    new1=TblData.objects.all()[2]
    return HttpResponse(f"Temperature = {new1.temperature}, Humidity = {new1.humidity}")
def getdata(request):
    item=TblData.objects.all()
    return render(request,'Home/Data-list.html',{'item':item})
def get1(request,dama,rotobat):
    from Home.models import TblData
    current_dateTime = datetime.now()
    new_data = TblData(temperature=dama, humidity=rotobat,timefild=current_dateTime.time(),Datefild=f"{current_dateTime.date()}")
    new_data.save()
    return HttpResponse(f'dama is {dama} & rotobat is {rotobat}')