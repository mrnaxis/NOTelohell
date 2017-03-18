from django.shortcuts import render

# Create your views here.
def loginC(request):
    return render(request, 'login.html')
