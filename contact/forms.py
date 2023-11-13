from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#criar um formulario django

class ContactForm(forms.ModelForm): #criar uma classe para formulario, dentro do parenteses é o herda esse ModelForm é um form baseado no modelo contact
    # first_name = forms.CharField(
    #     widget = forms.TextInput(
    #         attrs = {
    #             'placeholder' : 'Aqui veio do forms',
    #         },
    #     ), #recrio o campo do meu forms, utilizando essa estrutura
    #     label = 'Primeiro Nome',
    #     help_text = 'Texto de ajuda para o usuário'
    # )

    #criando o campo da imagem
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept' : 'image/*'
            }
        )
    )

    class Meta:
        model = Contact #indicamos em qual modelo o nosso form será baseado, e indicaremos quais campos serão exibidos
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
            'picture',
        ) #agora devemos passar o formulario no contexto para usarmos no site
 #adicionando erros no formulario
        #posso configurar o widgets do form, mudar o tipo de input por exemplo

        widgets = {
            'first_name' : forms.TextInput(
                attrs = { #referente a atributos do meu widget
                    'placeholder' : 'Type here...',
                }
            ),
        }

    '''
    def clean(self): #validação do formulario, TEM ACESSO A TODOS OS CAMPOS DO FORMULÁRIO
        #cleaned_data = self.cleaned_data

        self.add_error( #evita o formulario ser salvo caso esteja com erro
            'first_name', #nome do campo
            ValidationError(
                'Mensagem de erro', #mensagem do erro e um código q eu escolher passar
                code='invalid'
            )
        )

        return super().clean()
        '''

    def clean_first_name(self): #posso dar um clean e o nome do campo para ele validar aquele campo
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            raise ValidationError(
                'Do not type ABC in this field!',
                code='invalid'
            )

        return first_name #devo retornar o valor do campo, é o valor que vai para o campo do formulario

    def clean(self): #validação do formulario para saber se o nome eh igual ao sobrenome
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'Primeiro nome nao pode ser igual ao ultimo',
                code='invalid'
            )

            self.add_error('first_name', msg)
            self.add_error('last_name', msg) #nome do campo e a msg

        return super().clean()

    #no clean retorno super().clean()
    # no clean de campo retorno o campo


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True, #n permite ficar vazio
        min_length=3,
        error_messages={
            'required' : 'Campo obrigatório!'
        }
    )
    
    last_name = forms.CharField(
        required=True, #n permite ficar vazio
        min_length=3,
        error_messages={
            'required' : 'Campo obrigatório!'
        }
    )
        
    email = forms.EmailField(
        required=True, #n permite ficar vazio
        min_length=3,
        error_messages={
            'required' : 'Campo obrigatório!'
        }
    )
    
    class Meta: #defino como eu quero meu formulario, a partir do momento q implemento a classe meta, devo escrever ela de cabo a rabo do 0
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username',
            'password1', 'password2'
        )
    
    def clean_email(self): #evitar email repetido
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists(): #verifica se existe algum usuario c este email
            self.add_error(
                'email',
                ValidationError(
                    'This email already exists!',
                    code='invalid'
                )
            )
        
        return email