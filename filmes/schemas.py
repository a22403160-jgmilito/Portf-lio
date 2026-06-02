from ninja import Schema
from typing import List, Optional
from datetime import date


class RealizadorSchema(Schema):
    id: int
    nome: str
    nacionalidade: str
    data_nascimento: Optional[date] = None


class RealizadorCreateSchema(Schema):
    nome: str
    nacionalidade: str
    data_nascimento: Optional[date] = None


class GeneroSchema(Schema):
    id: int
    nome: str
    descricao: str


class GeneroCreateSchema(Schema):
    nome: str
    descricao: str = ""


class AtorSchema(Schema):
    id: int
    nome: str
    nacionalidade: str
    data_nascimento: Optional[date] = None


class AtorCreateSchema(Schema):
    nome: str
    nacionalidade: str
    data_nascimento: Optional[date] = None


class FilmeSchema(Schema):
    id: int
    titulo: str
    sinopse: str
    ano_lancamento: int
    duracao_minutos: int
    classificacao: float
    realizador_id: int
    generos: List[int]
    atores: List[int]


class FilmeCreateSchema(Schema):
    titulo: str
    sinopse: str
    ano_lancamento: int
    duracao_minutos: int
    classificacao: float = 0
    realizador_id: int
    generos: List[int] = []
    atores: List[int] = []