from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from documentos.models import Documentos
from documentos.forms import DocumentosForm





# Create your views here.
def show_dashboard(request):
    return render(request, 'dashboard.html');