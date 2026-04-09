import json
from pathlib import Path

from portfolio.models import TFC, Tecnologia


BASE_DIR = Path(__file__).resolve().parent.parent
JSON_PATH = BASE_DIR / "data" / "tfcs_2024_2025.json"


def limpar_texto_lista(valor):
    if not valor:
        return ""
    if isinstance(valor, list):
        return ", ".join(item.strip().rstrip(".") for item in valor if item)
    return str(valor).strip()


def limpar_url(valor):
    if not valor:
        return None
    valor = str(valor).strip()
    return valor if valor else None


def carregar_tfcs():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        tfcs = json.load(f)

    # opcional: limpar tudo antes de importar
    TFC.objects.all().delete()

    for item in tfcs:
        titulo = item.get("titulo", "").strip()
        if not titulo:
            continue

        ano = str(item.get("ano", "")).strip()
        licenciatura = item.get("licenciatura", "")
        sumario = item.get("sumario", "")
        link_pdf = limpar_url(item.get("link_pdf"))
        imagem = limpar_url(item.get("imagem"))
        palavras_chave = limpar_texto_lista(item.get("palavras_chave"))
        areas = limpar_texto_lista(item.get("areas"))
        rating = item.get("rating", 0)

        tfc = TFC.objects.create(
            titulo=titulo,
            ano=ano,
            licenciatura=licenciatura,
            sumario=sumario,
            link_pdf=link_pdf,
            imagem=imagem,
            palavras_chave=palavras_chave,
            areas=areas,
            rating=rating,
        )

        tecnologias_json = item.get("tecnologias", [])
        if isinstance(tecnologias_json, str):
            tecnologias_json = [t.strip() for t in tecnologias_json.split(",") if t.strip()]

        for nome_tec in tecnologias_json:
            nome_tec = nome_tec.strip().rstrip(".")
            if not nome_tec:
                continue

            tecnologia, _ = Tecnologia.objects.get_or_create(
                nome=nome_tec,
                defaults={
                    "tipo": "Outro",
                    "descricao": "Importada automaticamente do JSON de TFCs.",
                    "site_oficial": "https://www.google.com",
                    "nivel_interesse": 3,
                    "logotipo": "tecnologias/default.png",
                },
            )
            tfc.tecnologias.add(tecnologia)

    print("Importação concluída com sucesso.")