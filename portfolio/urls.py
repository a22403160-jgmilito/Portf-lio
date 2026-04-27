from django.urls import path
from . import views

urlpatterns = [
    path('projetos/', views.projetos_view, name='projetos'),
    path('projeto/novo/', views.novo_projeto_view, name='novo_projeto'),
    path('projeto/<int:projeto_id>/edita/', views.edita_projeto_view, name='edita_projeto'),
    path('projeto/<int:projeto_id>/apaga/', views.apaga_projeto_view, name='apaga_projeto'),
]