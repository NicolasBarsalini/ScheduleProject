from django.urls import path
from contact import views

app_name = 'contact' #criar um app name de contact

urlpatterns = [
    path('', views.index, name='index'), #criar a view
]