from django.shortcuts import render, get_object_or_404 #ela pega o objeto ou acusa um erro de 404
from contact.models import Contact
from django.http import Http404

def index(request):
    contacts = Contact.objects.filter(show=True)\
        .order_by('-id')[10:20] #coleto todos os contatos que permitem serem vistos e ordeno eles pelo ID de forma descrescente
     #\ indica continuacao na linha de baixo
     #[:10] fatio a minha informação, seleciono meus 10 primeiros valores
     #[10:20], começa do 10 e vai até o 20
     
    context = {
        'contacts' : contacts,
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