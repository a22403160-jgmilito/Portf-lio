import json
import os
from portfolio.models import Licenciatura, UnidadeCurricular

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES_PATH = os.path.join(BASE_DIR, 'files')


def carregar_ucs():
    ficheiro = os.path.join(FILES_PATH, 'ULHT260-PT.json')

    with open(ficheiro, encoding='utf-8') as f:
        dados = json.load(f)

    # Criar licenciatura
    nome_curso = dados.get("courseName", "Curso Desconhecido")

    licenciatura, _ = Licenciatura.objects.get_or_create(
        nome=nome_curso,
        defaults={
            "instituicao": "Universidade Lusófona",
            "duracao": 3,
            "descricao": "Importado automaticamente"
        }
    )

    # Criar UCs
    for uc in dados.get("courseFlatPlan", []):
        nome = uc.get("curricularUnitName")
        codigo = uc.get("curricularIUnitReadableCode")
        ects = uc.get("ects", 0)
        ano = uc.get("curricularYear", 1)
        semestre = uc.get("semester", "")

        UnidadeCurricular.objects.get_or_create(
            codigo=codigo,
            defaults={
                "nome": nome,
                "ects": ects,
                "ano": ano,
                "semestre": semestre,
                "licenciatura": licenciatura
            }
        )

    print("UCs importadas com sucesso!")