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