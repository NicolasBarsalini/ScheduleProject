from django.urls import path
from contact import views

app_name = 'contact' #criar um app name de contact

urlpatterns = [
    path('<int:contact_id>/', views.contact, name='contact'), # type: ignore
    #<> recebo um parametro dinamico do tipo inteiro e de nome contact_id
    path('', views.index, name='index'), #criar a view # type:ignor
]