from django.db import models


class Realizador(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Genero(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Ator(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Filme(models.Model):
    titulo = models.CharField(max_length=150)
    sinopse = models.TextField()
    ano_lancamento = models.IntegerField()
    duracao_minutos = models.IntegerField()
    classificacao = models.FloatField(default=0)

    realizador = models.ForeignKey(
        Realizador,
        on_delete=models.CASCADE,
        related_name='filmes'
    )

    generos = models.ManyToManyField(
        Genero,
        related_name='filmes'
    )

    atores = models.ManyToManyField(
        Ator,
        through='FilmeAtor',
        related_name='filmes'
    )

    def __str__(self):
        return self.titulo

class FilmeAtor(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    ator = models.ForeignKey(Ator, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ator.nome} em {self.filme.titulo}"
