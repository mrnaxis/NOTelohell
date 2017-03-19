from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def registrar(request): #melhor mudar para uma classe de view?
    return render(request, 'registrar.html')
