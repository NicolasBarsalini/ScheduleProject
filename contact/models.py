from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
    db_table = ''
    managed = True
    verbose_name = 'ModelName'
    verbose_name_plural = 'ModelNames'
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name

class Contact(models.Model): #herda do models model, sintetizo uma tabela a partir disso
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts' #corrije como fica ilustrado a descrição la no admin
        
    first_name = models.CharField(max_length=50) #sao por padrao obrigatorios caso estejam cadastrados aqui
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50) #o campo se torna opcional
    email = models.EmailField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now) #valor padrao ao registrar no banc de dados
    description = models.TextField(blank=True)
    #uma string na base de dados do tipo charfield eh limitada um text field nao tenho q passar a limitacao
    #id n precisa colocar pois eh automatico
    #criar uma migration sempre ao editar o model
    show = models.BooleanField(default=True) #saber se eu quero ou nao exibir o contato
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/') #upload_to fala onde deve ser enviada a imagem
    #%Y = ano, m = month
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True) #indico para qual eh apontada a chave e o que acontece ao apagar um contato
    #models.CASCADE fala que se você apagar a categoria, todos seus contatos pertecentes a ela serao deletados
    #setNULL = quando você deleta a categoria, os campos q usam ela serão considerados como null, permito que o campos esteja em branco e que seja nulo
    
    #criar o owner, o usuario que crio o contato consegue editar-lo ou remover-lo
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self) -> str: #indica que retorna uma string
        return f"{self.first_name} {self.last_name}" #imprime o str la no admin do django
    
    