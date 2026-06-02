from ninja import NinjaAPI
from typing import List
from django.shortcuts import get_object_or_404

from .models import Realizador, Genero, Ator, Filme
from .schemas import (
    RealizadorSchema,
    RealizadorCreateSchema,
    GeneroSchema,
    GeneroCreateSchema,
    AtorSchema,
    AtorCreateSchema,
    FilmeSchema,
    FilmeCreateSchema,
)

api = NinjaAPI()

def filme_para_dict(filme):
    return {
        "id": filme.id,
        "titulo": filme.titulo,
        "sinopse": filme.sinopse,
        "ano_lancamento": filme.ano_lancamento,
        "duracao_minutos": filme.duracao_minutos,
        "classificacao": filme.classificacao,
        "realizador_id": filme.realizador_id,
        "generos": list(filme.generos.values_list("id", flat=True)),
        "atores": list(filme.atores.values_list("id", flat=True)),
    }

# REALIZADORES

@api.get("/realizadores", response=List[RealizadorSchema], tags=["Realizadores"])
def listar_realizadores(request, nome: str = None, nacionalidade: str = None, offset: int = 0, limit: int = 10):
    realizadores = Realizador.objects.all()

    if nome:
        realizadores = realizadores.filter(nome__icontains=nome)

    if nacionalidade:
        realizadores = realizadores.filter(nacionalidade__icontains=nacionalidade)

    return realizadores[offset:offset + limit]


@api.post("/realizadores", response=RealizadorSchema, tags=["Realizadores"])
def criar_realizador(request, data: RealizadorCreateSchema):
    return Realizador.objects.create(**data.dict())


@api.get("/realizadores/{realizador_id}", response=RealizadorSchema, tags=["Realizadores"])
def obter_realizador(request, realizador_id: int):
    return get_object_or_404(Realizador, id=realizador_id)


@api.put("/realizadores/{realizador_id}", response=RealizadorSchema, tags=["Realizadores"])
def atualizar_realizador(request, realizador_id: int, data: RealizadorCreateSchema):
    realizador = get_object_or_404(Realizador, id=realizador_id)

    for campo, valor in data.dict().items():
        setattr(realizador, campo, valor)

    realizador.save()
    return realizador


@api.delete("/realizadores/{realizador_id}", tags=["Realizadores"])
def apagar_realizador(request, realizador_id: int):
    realizador = get_object_or_404(Realizador, id=realizador_id)
    realizador.delete()
    return {"success": True}


# GÉNEROS

@api.get("/generos", response=List[GeneroSchema], tags=["Géneros"])
def listar_generos(request, nome: str = None, offset: int = 0, limit: int = 10):
    generos = Genero.objects.all()

    if nome:
        generos = generos.filter(nome__icontains=nome)

    return generos[offset:offset + limit]

@api.post("/generos", response=GeneroSchema, tags=["Géneros"])
def criar_genero(request, data: GeneroCreateSchema):
    return Genero.objects.create(**data.dict())


@api.get("/generos/{genero_id}", response=GeneroSchema, tags=["Géneros"])
def obter_genero(request, genero_id: int):
    return get_object_or_404(Genero, id=genero_id)


@api.put("/generos/{genero_id}", response=GeneroSchema, tags=["Géneros"])
def atualizar_genero(request, genero_id: int, data: GeneroCreateSchema):
    genero = get_object_or_404(Genero, id=genero_id)

    for campo, valor in data.dict().items():
        setattr(genero, campo, valor)

    genero.save()
    return genero


@api.delete("/generos/{genero_id}", tags=["Géneros"])
def apagar_genero(request, genero_id: int):
    genero = get_object_or_404(Genero, id=genero_id)
    genero.delete()
    return {"success": True}


# ATORES

@api.get("/atores", response=List[AtorSchema], tags=["Atores"])
def listar_atores(request, nome: str = None, nacionalidade: str = None, offset: int = 0, limit: int = 10):
    atores = Ator.objects.all()

    if nome:
        atores = atores.filter(nome__icontains=nome)

    if nacionalidade:
        atores = atores.filter(nacionalidade__icontains=nacionalidade)

    return atores[offset:offset + limit]

@api.post("/atores", response=AtorSchema, tags=["Atores"])
def criar_ator(request, data: AtorCreateSchema):
    return Ator.objects.create(**data.dict())


@api.get("/atores/{ator_id}", response=AtorSchema, tags=["Atores"])
def obter_ator(request, ator_id: int):
    return get_object_or_404(Ator, id=ator_id)


@api.put("/atores/{ator_id}", response=AtorSchema, tags=["Atores"])
def atualizar_ator(request, ator_id: int, data: AtorCreateSchema):
    ator = get_object_or_404(Ator, id=ator_id)

    for campo, valor in data.dict().items():
        setattr(ator, campo, valor)

    ator.save()
    return ator


@api.delete("/atores/{ator_id}", tags=["Atores"])
def apagar_ator(request, ator_id: int):
    ator = get_object_or_404(Ator, id=ator_id)
    ator.delete()
    return {"success": True}


# FILMES

@api.get("/filmes", response=List[FilmeSchema], tags=["Filmes"])
def listar_filmes(request, titulo: str = None, ano_lancamento: int = None, offset: int = 0, limit: int = 10):
    filmes = Filme.objects.all()

    if titulo:
        filmes = filmes.filter(titulo__icontains=titulo)

    if ano_lancamento:
        filmes = filmes.filter(ano_lancamento=ano_lancamento)

    filmes = filmes[offset:offset + limit]

    return [filme_para_dict(filme) for filme in filmes]

@api.post("/filmes", response=FilmeSchema, tags=["Filmes"])
def criar_filme(request, data: FilmeCreateSchema):
    dados = data.dict()

    generos = dados.pop("generos")
    atores = dados.pop("atores")

    filme = Filme.objects.create(**dados)

    filme.generos.set(generos)
    filme.atores.set(atores)

    return filme_para_dict(filme)


@api.get("/filmes/{filme_id}", response=FilmeSchema, tags=["Filmes"])
def obter_filme(request, filme_id: int):
    filme = get_object_or_404(Filme, id=filme_id)
    return filme_para_dict(filme)


@api.put("/filmes/{filme_id}", response=FilmeSchema, tags=["Filmes"])
def atualizar_filme(request, filme_id: int, data: FilmeCreateSchema):
    filme = get_object_or_404(Filme, id=filme_id)

    dados = data.dict()

    generos = dados.pop("generos")
    atores = dados.pop("atores")

    for campo, valor in dados.items():
        setattr(filme, campo, valor)

    filme.save()

    filme.generos.set(generos)
    filme.atores.set(atores)

    return filme_para_dict(filme)


@api.delete("/filmes/{filme_id}", tags=["Filmes"])
def apagar_filme(request, filme_id: int):
    filme = get_object_or_404(Filme, id=filme_id)
    filme.delete()
    return {"success": True}