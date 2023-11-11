from django.urls import path
from contact import views

app_name = 'contact' #criar um app name de contact

urlpatterns = [
    path('contact/create/', views.create, name='contact'), #para criar um contato n preciso de um id
    path('', views.index, name='index'), #criar a view # type:ignor
    path('search/', views.search, name='search'),
    
    #<> recebo um parametro dinamico do tipo inteiro e de nome contact_id
    # contact (CRUD -> eu quero ler um contato, atualizar um contato, excluir um contato, adicionar um contato, etc...)
    path('contact/<int:contact_id>/detail/', views.contact, name='contact'), # type: ignore
    #path('contact/<int:contact_id>/update/', views.contact, name='contact'),
   # path('contact/<int:contact_id>/delete/', views.contact, name='contact'),
]