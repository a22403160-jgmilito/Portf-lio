from django.shortcuts import render, redirect, get_object_or_404
from .models import Projeto, Tecnologia, Competencia, Formacao
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm

# Create your views here.

def projetos_view(request):
    projetos = Projeto.objects.all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})

def novo_projeto_view(request):
    form = ProjetoForm(request.POST or None, request.FILES)

    if form.is_valid():
        form.save()
        return redirect('projetos')

    return render(request, 'portfolio/novo_projeto.html', {'form': form})

def edita_projeto_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)

    form = ProjetoForm(request.POST or None, request.FILES, instance=projeto)

    if form.is_valid():
        form.save()
        return redirect('projetos')

    return render(request, 'portfolio/edita_projeto.html', {'form': form, 'projeto': projeto})

def apaga_projeto_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    projeto.delete()
    return redirect('projetos')

def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/tecnologias.html', {'tecnologias': tecnologias})


def nova_tecnologia_view(request):
    form = TecnologiaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('tecnologias')
    return render(request, 'portfolio/nova_tecnologia.html', {'form': form})


def edita_tecnologia_view(request, tecnologia_id):
    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)
    form = TecnologiaForm(request.POST or None, request.FILES, instance=tecnologia)

    if form.is_valid():
        form.save()
        return redirect('tecnologias')

    return render(request, 'portfolio/edita_tecnologia.html', {'form': form})


def apaga_tecnologia_view(request, tecnologia_id):
    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)
    tecnologia.delete()
    return redirect('tecnologias')

def competencias_view(request):
    competencias = Competencia.objects.all()
    return render(request, 'portfolio/competencias.html', {'competencias': competencias})


def nova_competencia_view(request):
    form = CompetenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('competencias')
    return render(request, 'portfolio/nova_competencia.html', {'form': form})


def edita_competencia_view(request, competencia_id):
    competencia = get_object_or_404(Competencia, id=competencia_id)
    form = CompetenciaForm(request.POST or None, instance=competencia)

    if form.is_valid():
        form.save()
        return redirect('competencias')

    return render(request, 'portfolio/edita_competencia.html', {'form': form})


def apaga_competencia_view(request, competencia_id):
    competencia = get_object_or_404(Competencia, id=competencia_id)
    competencia.delete()
    return redirect('competencias')

def formacoes_view(request):
    formacoes = Formacao.objects.all()
    return render(request, 'portfolio/formacoes.html', {'formacoes': formacoes})


def nova_formacao_view(request):
    form = FormacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('formacoes')
    return render(request, 'portfolio/nova_formacao.html', {'form': form})


def edita_formacao_view(request, formacao_id):
    formacao = get_object_or_404(Formacao, id=formacao_id)
    form = FormacaoForm(request.POST or None, instance=formacao)

    if form.is_valid():
        form.save()
        return redirect('formacoes')

    return render(request, 'portfolio/edita_formacao.html', {'form': form})


def apaga_formacao_view(request, formacao_id):
    formacao = get_object_or_404(Formacao, id=formacao_id)
    formacao.delete()
    return redirect('formacoes')

def sobre_view(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/sobre.html', {'tecnologias': tecnologias})