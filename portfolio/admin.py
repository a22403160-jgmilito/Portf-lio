from django.contrib import admin
from .models import Licenciatura
from .models import UnidadeCurricular
from .models import Tecnologia
from .models import Competencia
from .models import Projeto 
from .models import Docente
from .models import Formacao
from .models import ExperienciaProfissional
from .models import TFC
from .models import MakingOf

# Register your models here.

admin.site.register(Licenciatura)
admin.site.register(UnidadeCurricular)
admin.site.register(Tecnologia)
admin.site.register(Competencia)
admin.site.register(Projeto)
admin.site.register(Docente)
admin.site.register(Formacao)
admin.site.register(ExperienciaProfissional)
admin.site.register(TFC)
admin.site.register(MakingOf)