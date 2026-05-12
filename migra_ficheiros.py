import os

from django.conf import settings
from django.core.files import File

from portfolio.models import (
    UnidadeCurricular,
    Tecnologia,
    Projeto,
    Docente,
    MakingOf
)

from escola.models import Curso


def migrar(modelo, campo):
    for obj in modelo.objects.all():

        ficheiro = getattr(obj, campo)

        if ficheiro and ficheiro.name:

            local_path = os.path.join(settings.MEDIA_ROOT, ficheiro.name)
            local_path = local_path.replace("media/media/", "media/")

            if os.path.exists(local_path):

                try:

                    with open(local_path, 'rb') as f:

                        ficheiro.save(
                            os.path.basename(local_path),
                            File(f),
                            save=True
                        )

                    print(f"Migrado: {modelo.__name__} -> {obj}")

                except Exception as e:
                    print(f"Erro em {obj}: {e}")

            else:
                print(f"Ficheiro não encontrado: {local_path}")


migrar(UnidadeCurricular, "imagem")
migrar(Tecnologia, "logotipo")
migrar(Projeto, "imagem")
migrar(Docente, "foto")
migrar(MakingOf, "imagem")
migrar(Curso, "imagem")

print("Migração concluída.")