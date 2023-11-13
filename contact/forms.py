from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

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
        ),
        required=False
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
    
class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.',
        error_messages={
            'min_length': 'Please, add more than 2 letters.'
        }
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.'
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label="Password 2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Use the same password as before.',
        required=False,
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username',
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('Senhas não batem')
                )

        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Já existe este e-mail', code='invalid')
                )

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error(
                    'password1',
                    ValidationError(errors)
                )

        return password1
