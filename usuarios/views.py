from django.shortcuts import render, redirect
from usuarios.forms import RegistrarForm
from django.views.generic.base import View
from django.contrib.auth.models import User

# Create your views here.
class RegistrarView(View):

    template_name = 'registrar.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = RegistrarForm(request.POST)
        if form.is_valid():
            formulario = form.data

            if (formulario['senha_user'] == formulario['senha_user_confirm']):
                usuario_dado = User.objects.create_user(formulario['nome_user'],
                formulario['email_user'], formulario['senha_user'], formulario['nick_user'])
            else:
                pass #adicionar excessao


def login(request):
    return render(request, 'login.html')

def usuario(request):
    return render(request, 'usuario.html')
