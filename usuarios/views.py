from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as loginAuth, logout as logoutAuth
from django.contrib.admin.views.decorators import staff_member_required 
from historico.views import adicionar_historico, remover_historico, atualiza_historico
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.decorators import login_required
from .serializer import UserSerializer
import rest_framework.permissions as permissions

@staff_member_required(login_url='/login')
def listar_usuarios(request):
  usuarios = User.objects.all()
  return render(request, 'usuarios.html', {'usuarios': usuarios})

@login_required(login_url="/login")
def atualizar_usuario(request, usuario_id):
   user = User.objects.filter(id=usuario_id).first() 
   
   if request.method == 'POST':
      userAntigo = User.objects.filter(id=usuario_id).first() 
      
      check = request.POST.get('admin') == 'on' if True else False
      user.username = request.POST.get('username')
      user.first_name = request.POST.get('primeiroNome')
      user.last_name = request.POST.get('sobrenome')
      if request.POST.get('senha'):        
        user.set_password(request.POST.get('senha'))
        
      user.email = request.POST.get('email')
      user.is_staff = check
      user.save()
      
      if request.user.username == '':
        atualiza_historico(user.username, 'Usuário', user, userAntigo)
      else:
        atualiza_historico(request.user, 'Usuário', user, userAntigo)
      
      if request.user.is_staff:
        usuarios = User.objects.all()
        return redirect('/usuarios', {'usuarios': usuarios})
      
      loginAuth(request, user)  
      return redirect('/')
      
   else:
      return render(request, 'cadastro.html', {'usuario': user})

@staff_member_required(login_url='/login')
def excluir_usuario(request, usuario_id):
  user = User.objects.filter(id=usuario_id).first() 
  user.delete()
  remover_historico(request.user.username, 'Usuário', usuario_id)
  
  usuarios = User.objects.all()
  return render(request, 'usuarios.html', {'usuarios': usuarios})

def cadastro(request):
  if request.method == 'GET':
    return render(request, 'cadastro.html')
  else:
    username = request.POST.get('username')
    primeiroNome = request.POST.get('primeiroNome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    check = request.POST.get('admin') == 'on' if True else False
    user = User.objects.filter(username=username, email=email).first()
    
    if user:
      user = ()
      return render(request, 'cadastro.html')
    else:      
      user = User.objects.create_user(username=username, email=email, password=senha, first_name=primeiroNome, last_name=sobrenome, is_staff=check)
      user.save()
            
      adicionar_historico(user.username, 'Usuário', user.id)
      return render(request, 'login.html')

def login(request):
  if request.method == 'GET':
    return render(request, 'login.html')
  else:
    username = request.POST.get('username')
    senha = request.POST.get('senha')
    
    user = authenticate(request, username=username, password=senha)
    
    if user is not None:
      loginAuth(request, user)  
      
      return redirect('/')
    else:
      return render(request, 'login.html', {'error': 'E-mail ou Senha invalidos'})

def logout(request):
  logoutAuth(request)
  return redirect('/')
# API
@swagger_auto_schema(methods=['GET'], operation_summary="Listar Todos os usuarios", tags=['Usuário'])
@api_view(['GET'])
@permission_classes([permissions.IsAdminUser]) 
def listar_usuariosJson(request):
    """
    Lista todos os usuários.
    """
    usuarios = User.objects.all()
    serializer = UserSerializer(usuarios, many=True)
    return Response(serializer.data)

@swagger_auto_schema(methods=['POST'], operation_summary="Cadastrar um novo Usuario", request_body=UserSerializer, tags=['Usuário'])
@api_view(['POST'])
@permission_classes([permissions.IsAdminUser]) 
def cadastroJson(request):
    """
    Cadastra um novo usuário.
    """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        adicionar_historico(request.user.username, 'Usuário', serializer.data['id'])
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(methods=['GET'], operation_summary="Detalhar um usuário", tags=['Usuário'])
@api_view(['GET'])
@permission_classes([permissions.IsAdminUser]) 
def detalhe_usuarioJson(request,usuario_id):
   """
   Retorna detalhes de um usuário específico
   """
   try:
      usuario = User.objects.get(pk=usuario_id)
   except User.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
   
   serializer=UserSerializer(usuario)
   return Response(serializer.data)

@swagger_auto_schema(methods=['PUT', 'PATCH'], operation_summary="Atualizar um usuario existente", request_body=UserSerializer, tags=['Usuário'])
@api_view(['PUT', 'PATCH'])
@permission_classes([permissions.IsAdminUser]) 
def atualizar_usuarioJson(request, usuario_id):
    """
    Atualiza os detalhes de um  usuário específico.
    """
    try:
        user = User.objects.get(pk = usuario_id)
    except User.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user, data=request.data, partial = True)
    if serializer.is_valid():
      userAntigo = User.objects.get(pk=usuario_id)
      serializer.save()
      atualiza_historico(request.user.username, 'Usuário', serializer, userAntigo)
      return Response(serializer.data)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(methods=['DELETE'], operation_summary="Exclui um usuario existente", request_body=UserSerializer, tags=['Usuário'])
@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser]) 
def excluir_usuarioJson(request, usuario_id):
   """
  Exclui um usuário   
   """
   try:
      user = User.objects.get(usuario_id = usuario_id)
   except User.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
   user_id = user.id
   user.delete()
   remover_historico(request.user.username, 'Usuário', user_id)
   return Response(status = status.HTTP_204_NO_CONTENT)



#def loginJson(request):
  
#def logoutJson(request):