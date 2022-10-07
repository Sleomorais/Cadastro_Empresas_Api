from django.contrib import admin
from .models import Empresa

class Empresas(admin.ModelAdmin):
    list_display = ('id', 'cnpj','nome_empresa', 'responsavel')
    list_display_links = ('id', 'nome_empresa',)
    list_per_page: 10

admin.site.register(Empresa,Empresas)
