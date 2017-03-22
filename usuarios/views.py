from django.shortcuts import render, redirect
from usuarios.forms import RegistrarForm
from django.views.generic.base import View
from django.contrib.auth.models import User
from dashboard.views import get_perfil_logado

# Create your views here.
class RegistrarView(View):

    template_name = 'registrar.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = RegistrarForm(request.POST)
        if form.is_valid():
            formulario = form.data
            usuario_dado = User.objects.create_user(formulario['nome_user'],formulario['email_user'],formulario['senha_user'])
            return redirect('login')
        return render(request, self.template_name, {'form' : form })


def login(request):
    return render(request, 'login.html')

def usuario(request):
    return render(request, 'usuario.html',{'perfil' : get_perfil_logado(request)})
