from django.contrib import admin
from .models import Realizador, Genero, Ator, Filme, FilmeAtor


class FilmeAtorInline(admin.TabularInline):
    model = FilmeAtor
    extra = 1


@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano_lancamento', 'realizador', 'classificacao')
    list_filter = ('ano_lancamento', 'generos')
    search_fields = ('titulo', 'realizador__nome')
    inlines = [FilmeAtorInline]
    filter_horizontal = ('generos',)


@admin.register(Realizador)
class RealizadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nacionalidade', 'data_nascimento')
    search_fields = ('nome',)


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


@admin.register(Ator)
class AtorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nacionalidade', 'data_nascimento')
    search_fields = ('nome',)


@admin.register(FilmeAtor)
class FilmeAtorAdmin(admin.ModelAdmin):
    list_display = ('filme', 'ator')
    search_fields = ('filme__titulo', 'ator__nome')