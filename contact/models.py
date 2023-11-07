from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model): #herda do models model, sintetizo uma tabela a partir disso
    first_name = models.CharField(max_length=50) #sao por padrao obrigatorios caso estejam cadastrados aqui
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50) #o campo se torna opcional
    email = models.EmailField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now()) #valor padrao ao registrar no banc de dados
    description = models.TextField(blank=True)
    #uma string na base de dados do tipo charfield eh limitada um text field nao tenho q passar a limitacao
    #id n precisa colocar pois eh automatico
    #criar uma migration sempre ao editar o model
    
    def __str__(self) -> str: #indica que retorna uma string
        return f"{self.first_name} {self.last_name}" #imprime o str la no admin do django