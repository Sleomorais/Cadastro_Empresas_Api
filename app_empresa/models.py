from enum import unique
from django.db import models

class Empresa(models.Model):
    cnpj = models.CharField(max_length = 14, unique = True)
    nome_empresa = models.CharField(max_length = 255)
    responsavel = models.CharField(max_length = 255)

    def __str__(self):
        return self.nome_empresa
