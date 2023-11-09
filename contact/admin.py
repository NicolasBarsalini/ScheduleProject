from django.contrib import admin
from contact import models

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin): #herda da classe de admin, devo atribuir ela no admin do django#cria no painel admin o contatos
    list_display = 'id', 'first_name', 'last_name', 'phone', 'show', 'email' #consigo mostrar do jeito que eu quiser esse padrão de ordenação
    ordering = '-id', #esse menos ordena pelo id de forma descrescente
    list_filter = 'created_date', #permite a filtragem da base de dados pelos dias
    search_fields = 'id', 'first_name', 'last_name', 'category'
    list_per_page = 15 #exibe x itens por pagina
    list_max_show_all = 200 #limita o mostrar tudo do django
    #list_editable = 'first_name', 'last_name' #permitem quais campos podem ser editados
    list_display_links = 'id', 'first_name', 'show' #permite que você escolha quais campos contenham o link para acesso de editar os dados
    
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',