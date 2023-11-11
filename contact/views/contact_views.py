from django.shortcuts import render, get_object_or_404, redirect #ela pega o objeto ou acusa um erro de 404
from contact.models import Contact
from django.db.models import Q
from django.core.paginator import Paginator
    
def index(request):
    '''contacts = Contact.objects.filter(show=True)\
        .order_by('-id')[10:20] #coleto todos os contatos que permitem serem vistos e ordeno eles pelo ID de forma descrescente
     #\ indica continuacao na linha de baixo
     #[:10] fatio a minha informação, seleciono meus 10 primeiros valores
     #[10:20], começa do 10 e vai até o 20'''
     
    contacts = Contact.objects.filter(show=True).order_by('-id')
    
    paginator = Paginator(contacts, 10) #objeto e quantidade de contato por pagina
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
     
    context = {
        'page_obj' : page_obj,
        'site_title' : 'Contatos - '
    }
    
    return render(
        request,
        'contact/index.html',
        context
    )

def contact(request, contact_id): #a url recebe uma requisicao e me envia um contact_id, eu recebo o contact_id e envio para o get
    #single_contact = Contact.objects.get(pk=contact_id) #retorna um unico valor
    #se o get n encontrar o valor na consulta ele laça um erro, para corrgir isso poderia usar um filter
    '''single_contact = Contact.objects.filter(pk=contact_id).first() #retorna uma query set(lista), porém pego o primeiro valor da lista, que corresponde a contato
    
    if single_contact is None:
        raise Http404()'''
        
    #single_contact = get_object_or_404(Contact.objects.filter(pk=contact_id)) #informo meu model e o valor que desejo filtrar
    #ou 
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True) #o show deve estar em true para eu exibir
    
    site_title = f"{single_contact.first_name} {single_contact.last_name} -"
    
    context = {
        'contact' : single_contact,
        'site_title' : site_title
    }
    
    return render(
        request,
        'contact/contact.html',
        context
    )
    
def search(request): # se a pessoa pesquisar no botão de search
    search_value = request.GET.get('q', '') #tento dar um get na chave q, se n vier nada eu recebo uma string vazia #retorna um query dict, um dicionario no python basicamente
    search_value.strip() #remove espaços do começo ao fim caso tenha algum
    print(search_value) #{'q': ['swf']}, essa chave é o name do meu form
    
    #se a pessoa mandar um valor vazio, eu redireciono ela por index
    if search_value == '':
        return redirect('contact:index') #redireciono para a home do site
    
    contacts = Contact.objects.filter(show=True)\
        .filter(
           Q(first_name__icontains=search_value) |  #só a virgula o comando usa and, eu estou fazendo uma busca para encontrar um nome que tenha %Nico% por exemplo
            Q(last_name__icontains=search_value) | #esse q faz o and virar or e dai removo a virgula e coloco |
            Q(email__icontains=search_value) |
            Q(phone__icontains=search_value)
        )\
        .order_by('-id')
        
    '''.filter(
           Q(first_name__icontains=search_value),  #só a virgula o comando usa and, eu estou fazendo uma busca para encontrar um nome que tenha %Nico% por exemplo
            Q(last_name__icontains=search_value), #esse q faz o and virar or e dai removo a virgula e coloco |
        )\
    '''
    
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Search - ',
        'search_value': search_value,
    }

    return render(
        request,
        'contact/index.html',
        context
    )
