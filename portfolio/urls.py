from django.urls import path
from . import views

urlpatterns = [
    path('projetos/', views.projetos_view, name='projetos'),
    path('projeto/novo/', views.novo_projeto_view, name='novo_projeto'),
    path('projeto/<int:projeto_id>/edita/', views.edita_projeto_view, name='edita_projeto'),
    path('projeto/<int:projeto_id>/apaga/', views.apaga_projeto_view, name='apaga_projeto'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('tecnologia/novo/', views.nova_tecnologia_view, name='nova_tecnologia'),
    path('tecnologia/<int:tecnologia_id>/edita/', views.edita_tecnologia_view, name='edita_tecnologia'),
    path('tecnologia/<int:tecnologia_id>/apaga/', views.apaga_tecnologia_view, name='apaga_tecnologia'),
    path('competencias/', views.competencias_view, name='competencias'),
    path('competencia/novo/', views.nova_competencia_view, name='nova_competencia'),
    path('competencia/<int:competencia_id>/edita/', views.edita_competencia_view, name='edita_competencia'),
    path('competencia/<int:competencia_id>/apaga/', views.apaga_competencia_view, name='apaga_competencia'),
    path('formacoes/', views.formacoes_view, name='formacoes'),
    path('formacao/novo/', views.nova_formacao_view, name='nova_formacao'),
    path('formacao/<int:formacao_id>/edita/', views.edita_formacao_view, name='edita_formacao'),
    path('formacao/<int:formacao_id>/apaga/', views.apaga_formacao_view, name='apaga_formacao'),
    path('sobre/', views.sobre_view, name='sobre'),
]