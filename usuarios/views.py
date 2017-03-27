from django.shortcuts import render, redirect
from usuarios.forms import RegistrarForm
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from usuarios.models import Usuario

# Create your views here.
class RegistrarView(View):

    template_name = 'registrar.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = RegistrarForm(request.POST)
        if form.is_valid():
            formulario = form.data

            usuario_dado = User.objects.create_user(formulario['email_user'],formulario['email_user'],formulario['senha_user'])
            usuario_final = Usuario(nome=formulario['nome_user'],nick=formulario['nick_user'], usuario=usuario_dado)

            usuario_final.save()
            return redirect('login')
        return render(request, self.template_name, {'form' : form })


def login(request):
    return render(request, 'login.html')

@login_required
def usuario(request):
    return render(request, 'usuario.html')

@login_required
def usuario_editar(request):
    return render(request, 'usuario_editar.html')
