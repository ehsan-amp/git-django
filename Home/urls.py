from django.urls import path
from . import views
urlpatterns = [
    path('home', views.home),
    path('Data', views.getdata),
path('<dama>/<rotobat>', views.get1),
]