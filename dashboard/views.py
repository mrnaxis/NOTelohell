from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# View para dashboard
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def get_usuario_logado(request):
    return request.user.usuario
