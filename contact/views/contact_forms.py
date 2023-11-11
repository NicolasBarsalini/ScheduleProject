from django.shortcuts import get_object_or_404, redirect, render
from contact.models import Contact

def create(request):
    #request.POST.get('nome_do_input'), retorna um query set
    first_name = request.POST.get('first_name')
    print(first_name)
    context = {
        
    }
    
    return render(
        request,
        'contact/create.html',
        context
    )