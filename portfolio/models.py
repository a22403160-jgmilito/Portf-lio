from django.db import models

# Create your models here.

class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    duracao = models.IntegerField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50)  # NOVO
    descricao = models.TextField(blank=True)
    ano = models.IntegerField()  # ano curricular
    semestre = models.CharField(max_length=20)  # "Semestral"
    ects = models.FloatField()  # NOVO
    imagem = models.ImageField(upload_to='ucs/', blank=True, null=True)
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE)
    docentes = models.ManyToManyField("Docente", blank=True)

    def __str__(self):
        return self.nome

class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    descricao = models.TextField()
    logotipo = models.ImageField(upload_to='tecnologias/', blank=True, null=True)
    site_oficial = models.URLField()
    nivel_interesse = models.IntegerField()

    def __str__(self):
        return self.nome

class Competencia(models.Model):
    nome = models.CharField(max_length=100)
    nivel = models.CharField(max_length=50)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='projetos/', null=True, blank=True)
    video_demo = models.URLField(null=True, blank=True)
    github_link = models.URLField(null=True, blank=True)
    unidade_curricular = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE)

    tecnologias = models.ManyToManyField(Tecnologia, blank=True)
    competencias = models.ManyToManyField(Competencia, blank=True)

    def __str__(self):
        return self.nome

class Docente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    pagina_lusofona = models.URLField()
    foto = models.ImageField(upload_to='docentes/', blank=True)

    def __str__(self):
        return self.nome

class Formacao(models.Model):
    nome = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    descricao = models.TextField()

    competencias = models.ManyToManyField(Competencia)

    def __str__(self):
        return self.nome

class ExperienciaProfissional(models.Model):
    empresa = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField()
    aprendizagem = models.TextField()

    competencias = models.ManyToManyField(Competencia)

    def __str__(self):
        return self.empresa

class TFC(models.Model):
    titulo = models.CharField(max_length=200)
    ano = models.CharField(max_length=20)
    licenciatura = models.CharField(max_length=150, blank=True)
    sumario = models.TextField(blank=True)
    link_pdf = models.URLField(blank=True, null=True)
    imagem = models.URLField(blank=True, null=True)
    palavras_chave = models.TextField(blank=True)
    areas = models.TextField(blank=True)
    rating = models.IntegerField(default=0)

    tecnologias = models.ManyToManyField(Tecnologia, blank=True)

    def __str__(self):
        return self.titulo
    
class MakingOf(models.Model):
    descricao = models.TextField()
    data = models.DateField()
    imagem = models.ImageField(upload_to='makingof/', blank=True)
    decisao = models.TextField()
    erro = models.TextField()
    correcao = models.TextField()

    projeto = models.ForeignKey("Projeto", on_delete=models.CASCADE, null=True, blank=True)
    tecnologia = models.ForeignKey("Tecnologia", on_delete=models.CASCADE, null=True, blank=True)
    unidade_curricular = models.ForeignKey("UnidadeCurricular", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.descricao[:50]