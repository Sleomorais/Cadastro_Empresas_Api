from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastro, name='cadastro'),
    path('empresa/', views.EmpresasAPIView.as_view(), name='empresa')
]