from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistoForm
from django.contrib.auth.models import Group

def login_view(request):

    erro = ""

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request,
                            username=username,
                            password=password)

        if user is not None:
            login(request, user)
            return redirect('projetos')

        else:
            erro = "Utilizador ou password inválidos"

    return render(request, 'accounts/login.html', {
        'erro': erro
    })


def logout_view(request):
    logout(request)
    return redirect('login')


def registo_view(request):

    form = RegistoForm(request.POST or None)

    if form.is_valid():

        user = form.save()

        grupo = Group.objects.get(name='autores')

        user.groups.add(grupo)

        return redirect('login')

    return render(request, 'accounts/registo.html', {
        'form': form
    })