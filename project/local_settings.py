SECRET_KEY = 'CHANGE-ME' #defino meu secret key aqui

#Qualquer coisa que estiver aqui, sera importado para o settings é bom para sobreescrever os dados do settings.py caso esteja em um ambiente local
DEBUG = True

ALLOWED_HOSTS: list[str] = [] #qualquer site eh de acesso permitido
#tipod e lista de string

#arquivos estaticos nao são carregados no debug = false