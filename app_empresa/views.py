from django.shortcuts import render, redirect
from .models import *
from rest_framework import generics, status
from django.contrib import messages
from .serializer import EmpresaSerializer

def cadastro(request):
    if request.method == 'POST':
        cnpj = request.POST['cnpj']
        nome_empresa = request.POST['nome_empresa']
        responsavel = request.POST['responsavel']
        empresa = Empresa.objects.filter(cnpj=cnpj).exists()
        if empresa == False and cnpj and nome_empresa and responsavel and cnpj.isdigit() and len(cnpj) == 14:
            empresa = Empresa.objects.create(cnpj = cnpj, nome_empresa = nome_empresa, responsavel = responsavel)
            empresa.save()
            return redirect('empresa/')
        else:
            messages.error(request, "Preencha os Dados Corretamente")
            return render(request,'cadastro.html')
    return render(request,'cadastro.html')

class EmpresasAPIView(generics.ListAPIView):
    """Exibindo As Empresas Na API"""
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
