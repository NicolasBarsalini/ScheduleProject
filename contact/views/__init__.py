#por eu ter mts views no contact e o codigo ficar muito grande, eu posso criar ele como um pacote que contem vaarios módulos e fazer o views.py funcionar no __init__.py
# flake8: noqa
#desabilito o flake 8 e ignoro as tipagens, só pra evitar problemas mesmo
# type: ignore
from .contact_forms import *
from .contact_views import * #importo tudo q tem dentro do módulo contact_views antes de qualquer coisa
from .user_forms import *