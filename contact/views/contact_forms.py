from django.shortcuts import get_object_or_404, redirect, render
from contact.forms import ContactForm
from django.urls import reverse
from contact.models import Contact

def create(request): 
    form_action = reverse('contact:create')
    #request.method() consigo saber se o metodo utilizado foi get ou post
    #request.POST.get('nome_do_input'), retorna um query set
    
    if request.method == 'POST':  
        form = ContactForm(request.POST, request.FILES)
        context = {
            'form' :  form,#quando eu mandar os atributos de volta do forms pra ca, eu quero que meu data receba os parametros colocados
            'form_action' : form_action,
        }
        
        if form.is_valid(): # se o formmulario eh valido, ou seja n tem erro, eu posso proseeguir para salvar na base de dados
            #metodo para salvar o formulario
            contact = form.save() #ja salvo os dados na base de dados
            # se eu fizer
            # contact = form.save(commit=False) #ele n salva na base dados, fica somente em memória
            # posso fazer por exemplo a alteração de um campo e dps salvar na base de dados
            # contact.show = False
            # contact.save()
            return redirect('contact:update', contact_id=contact.pk) #url e em seguida o paramêtro dinamico ou contact.id
            
        return render(
            request,
            'contact/create.html',
            context
        )
        
    context = {
        'form' : ContactForm(), #este eh um formulario limpo, q n foi postado, só quando o método é get ele monta o formulario na minha tela
        'form_action' : form_action,
    }
        
    return render(
        request,
        'contact/create.html',
        context
    )
    
def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse('contact:update', args=(contact_id,)) #passo io parametro dinamico da url
    
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact) #essa instancia fala q ja tenho os dados dess contato e o que vier no data no post eh pra atualizar

        context = {
            'form' : form,
            'form_action' : form_action,
        }
        
        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)
        
        return render(
            request,
            'contact/create.html',
            context
        )
        
    context = {
        'form' : ContactForm(instance=contact), #preenchendo a instancia do contato no formulario
        'form_action' : form_action
    }
        
    return render(
        request,
        'contact/create.html',
        context
    )


def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True
    )
    
    confirmation = request.POST.get('confirmation', 'no') #pego o valor do input confirmation, se n encontrar valor, confirmation por padrao é igual a no
    
    if confirmation == 'yes':   
        contact.delete()
        return redirect('contact:index')
    
    return render(
        request,
        'contact/contact.html',
        context = {
            'contact' : contact,
            'confirmation' : confirmation,
        }
    )
