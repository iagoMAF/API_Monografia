from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as loginAuth, logout as logoutAuth
from django.urls import include

# Create your views here.
def cadastro(request):
  if request.method == 'GET':
    return render(request, 'cadastro.html')
  else:
    username = request.POST.get('username')
    primeiroNome = request.POST.get('primeiroNome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    confirmaSenha = request.POST.get('confirmaSenha')
    user = User.objects.filter(username=username, email=email).first()
    
    if user:
      user = ()
      return render(request, 'cadastro.html')
    else:
      if senha!= confirmaSenha:
        return render(request, 'cadastro.html')
      
      user = User.objects.create_user(username=username, email=email, password=senha, first_name=primeiroNome, last_name=sobrenome)
      user.save()
      return render(request, 'login.html', {'user': user})
    

def login(request):
  if request.method == 'GET':
    return render(request, 'login.html')
  else:
    username = request.POST.get('username')
    senha = request.POST.get('senha')
    
    user = authenticate(request, username=username, password=senha)
    
    if user is not None:
      loginAuth(request, user)  
      
      return render(request, 'index.html')
    else:
      return render(request, 'login.html', {'error': 'E-mail ou Senha invalidos'})
    
def logout(request):
  logoutAuth(request)
  return render(request, 'index.html')