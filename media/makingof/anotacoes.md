MODELAGEM INICIAL – PORTFÓLIO
Entidades:
- Licenciatura
- UnidadeCurricular
- Projeto
- Tecnologia
- TFC
- Competencia
- Formacao
- Docente
- MakingOf
- (Extra) ExperienciaProfissional, Decidi incluir ExperienciaProfissional para enriquecer o portfólio além do contexto académico.

ATRIBUTOS:

Observação:
Ao declarar os atributos de cada entidade, 
pus o atributo e separando com uma "," expliquei o pq do atributo

Entidade: UnidadeCurricular
- id
- nome, identifica claramente a UC
- descrição, permite explicar o conteúdo
- ano, organiza cronologicamente
- semestre, organiza cronologicamente
- imagem, melhora apresentação visual

Entidade: Licenciatura
- id
- nome, identificar curso
- instituição, contexto académico
- duração, estrutura do curso
- descrição, informação adicional

Entidade: Docente
- id
- nome
- email, contacto
- pagina lusófona, ligação oficial
- foto, parte visual

Entidade: Projeto
- id
- nome
- descrição, permite explicar o conteúdo
- imagem, melhora apresentação visual
- video_demo, demonstra funcionamento
- github_link, importante para emprego

Entidade: Tecnologia
- id
- nome
- tipo (linguagem, framework, etc.), organizar melhor
- descrição, permite explicar brevemente o conteúdo 
- logotipo, parte visual 
- site oficial, mostra o empenho em explicar da onde vem a informação 
- nivel_interesse (1-5), mostra nível se experiencia/conhecimento 

Entidade: TFC
- id
- titulo
- descrição, permite explicar o conteúdo
- ano, organiza cronologicamente
- classificação, destacar os melhores

Entidade: Competencia
- id
- nome
- nivel (iniciante/intermedio/avancado), mostra nível se experiencia/conhecimento 
- descrição, permite explicar brevemente o conteúdo 

Entidade: Formacao
- id
- nome
- instituição
- data_inicio
- data_fim
- descrição, permite explicar o que eu fiz e o que aprendi

Entidade: MakingOf
- id
- descrição,  permite explicar o que eu fiz
- data, organiza cronologicamente
- imagem, prova de trabalho manual
- decisão 
- erro, mostra aprendizagem
- correção, mostra aprendizagem

Entidade: ExperienciaProfissional
- id
- empresa
- cargo
- descrição, permite explicar o que eu fiz
- data_inicio
- data_fim
- aprendizagem, permite eu explicar o que aprendi e o que ganhei ao trabalhar em determinada empresa 


RELAÇÕES: 


UnidadeCurricular 1 --- N Projeto
UnidadeCurricular N --- N Docente

Licenciatura 1 --- N UnidadeCurricular

Projeto N --- N Tecnologia
Projeto N --- N Competencia

Tecnologia N --- N Competencia

Formacao N --- N Competencia

ExperienciaProfissional N --- N Competencia

TFC N --- N Tecnologia


MakingOf N --- 1 Competencia
MakingOf N --- 1 Projeto
MakingOf N --- 1 Tecnologia
MakingOf N --- 1 UnidadeCurricular
MakingOf N --- 1 Licenciatura
MakingOf N --- 1 Formação
MakingOf N --- 1 ExperienciaProfissional
MakingOf N --- 1 Docente
MakingOf N --- 1 TFC

Explicações sobre as relações e alguns apontamentos:

Projeto ↔ Tecnologia:

Um projeto pode usar várias tecnologias e uma tecnologia pode estar em vários projetos.
UC ↔ Docente:
Uma UC pode ter vários docentes.
Projeto ↔ Competência:
Projetos desenvolvem competências.
TFCs utilizam tecnologias, tal como projetos.
Inicialmente defini tecnologias como atributo, mas corrigi para relação N:N por representar melhor a realidade.
Optei por associar o MakingOf apenas a algumas entidades principais para simplificar a implementação em Django, 
mantendo a flexibilidade de documentar o processo de desenvolvimento.
Os modelos Django foram definidos com base no DER desenvolvido anteriormente, 
respeitando as relações 1:N (ForeignKey) e N:N (ManyToManyField), garantindo coerência entre a modelagem conceptual e a implementação.

Relações N:N foram implementadas com ManyToManyField:
Projeto ↔ Tecnologia:
tecnologias = models.ManyToManyField(Tecnologia)

Projeto ↔ Competência:
competencias = models.ManyToManyField(Competencia)

UC ↔ Docente:
docentes = models.ManyToManyField(Docente)

Tecnologia ↔ Competência:
competencias = models.ManyToManyField(Competencia)

Formacao ↔ Competência:
competencias = models.ManyToManyField(Competencia)

Experiencia ↔ Competência:
competencias = models.ManyToManyField(Competencia)

TFC ↔ Tecnologia:
tecnologias = models.ManyToManyField(Tecnologia)

Embora no modelo conceptual o MakingOf esteja associado a várias entidades, 
na implementação em Django optei por associar apenas às entidades principais 
(Projeto, Tecnologia e UnidadeCurricular) para simplificar o modelo e evitar 
complexidade excessiva.

Na parte que criei as classes no meu portifólio em Django eu as vezes chamava pela classe,
e as vezes por String, pois em py se le de cima para baixo, logo se eu usasse uma classe em cima me referindo a uma classe embaixo
iria dar erro, NameError: name 'xxxxx' is not defined, onde o "xxxxx" seria o nome da classe que estava chamando,
esse erro da normalmente quando estou fazendo as ligações entre classes, usando ForeignKey e ManyToManyField.

Em relacao a parte do JSON:
Usei ano como CharField, porque o meu JSON usa valores como "2024-2025" e não um inteiro simples.
Usei palavras_chave e areas como TextField, porque no JSON elas vêm como listas, e é mais simples guardar como texto separado por vírgulas do que criar novas entidades só para isso.

Foi desenvolvido um script em Python (loader.py) que lê um ficheiro JSON contendo os TFCs extraídos por web scraping.
Utilizando o ORM do Django, os dados foram inseridos na base de dados de forma estruturada.
Durante o processo surgiram alguns erros:
- Caminho incorreto do ficheiro JSON (FileNotFoundError)
- Tipo de dados errados no campo "ano"

Estes erros foram analisados e corrigidos, levando à melhoria da modelação.
Foi também implementada uma relação ManyToMany entre TFC e Tecnologias, 
permitindo representar corretamente as tecnologias usadas em cada projeto.

Eu quando fiz o commit para o repositorio no GitHub, em relacao a parte da importacao do JSON para a base de dados,
eu acabei so copiando e colando os comandos que o professor disponibilizou, e o a mensagem ficou sem significado, ficou a que o professor disse,
"mensagem que descreve o que fez", mas a mensagem que queria usar era "Importacao de TFCs via JSON e integracao com base de dados", fui fazer no automatico 
e me equivoquei, falta de atencao.

Em relacao ao carregamento de dados de Curso e Unidades Curriculares:
Após analisar os dados da API da Lusófona, verifiquei que existiam atributos relevantes nas unidades curriculares que não estavam presentes na modelação inicial, como o código da UC, os ECTS e o ano curricular.

Decidi adicionar esses atributos ao modelo UnidadeCurricular, de forma a representar melhor a estrutura real do curso e enriquecer a informação disponível na aplicação.

Foi desenvolvido um script para importar automaticamente dados das unidades curriculares a partir da API da Universidade Lusófona.
Isto permitiu garantir dados reais e atualizados, evitando inserção manual e aumentando a consistência da informação.
Foi utilizada a função get_or_create para evitar duplicação de dados.

EVOLUÇÃO DO MODELO:

Versão 1:
Modelo inicial com tecnologias como atributo.

Versão 2:
Correção para relação ManyToMany.

Versão 3:
Adição da entidade ExperienciaProfissional.

Versão 4:
Ajuste das relações do MakingOf para simplificação.

Durante o desenvolvimento utilizei ferramentas de IA como apoio à compreensão 
de conceitos e validação da modelação.

A IA foi utilizada principalmente para:
- esclarecer dúvidas sobre Django
- validar relações entre entidades
- apoiar na implementação dos modelos

No entanto, todas as decisões de modelação foram analisadas e ajustadas 
manualmente, garantindo coerência com os requisitos do projeto.

MODELOS DJANGO:

Licenciatura:

class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    duracao = models.IntegerField()
    descricao = models.TextField()

UnidadeCurricular:

relação:
Licenciatura 1 → N UnidadeCurricular

class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    ano = models.IntegerField()
    semestre = models.IntegerField()
    imagem = models.ImageField(upload_to='ucs/')

    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE)
    docentes = models.ManyToManyField(Docente)

Docente:

class Docente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    pagina_lusofona = models.URLField()
    foto = models.ImageField(upload_to='docentes/')

Projeto:

relação:
UC 1 → N Projeto

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='projetos/')
    video_demo = models.URLField()
    github_link = models.URLField()

    unidade_curricular = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE)
    tecnologias = models.ManyToManyField(Tecnologia)
    competencias = models.ManyToManyField(Competencia)

Tecnologia:

class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    descricao = models.TextField()
    logotipo = models.ImageField(upload_to='tecnologias/')
    site_oficial = models.URLField()
    nivel_interesse = models.IntegerField()

Competência:

class Competencia(models.Model):
    nome = models.CharField(max_length=100)
    nivel = models.CharField(max_length=50)
    descricao = models.TextField()

Formação:

class Formacao(models.Model):
    nome = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    descricao = models.TextField()
  
    competencias = models.ManyToManyField(Competencia)

TFC:

class TFC(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    ano = models.IntegerField()
    classificacao = models.FloatField()

    tecnologias = models.ManyToManyField(Tecnologia)

ExperienciaProfissional:

class ExperienciaProfissional(models.Model):
    empresa = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField()
    aprendizagem = models.TextField()

    competencias = models.ManyToManyField(Competencia)

MakingOf:

class MakingOf(models.Model):
    descricao = models.TextField()
    data = models.DateField()
    imagem = models.ImageField(upload_to='makingof/')
    decisao = models.TextField()
    erro = models.TextField()
    correcao = models.TextField()

    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, null=True, blank=True)
    tecnologia = models.ForeignKey(Tecnologia, on_delete=models.CASCADE, null=True, blank=True)
    unidade_curricular = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE, null=True, blank=True)

Ultimos apontamentos:

Apos evolucoes do projeto e analise de infomarcoes, foram necessarias algumas alteracoes 
na parte dos modelos Django, e possivelmente ira se alterar ao decorrer dos anos tambem. 
Ainda sao necessarios criar novas componetes, projetos, entre outros atributos na parte do site, pois nao tenho todos
os links ou videos dos meus projetos, mas isso sao coisas que iram se evoluindo e se construindo ao decorrer dos semestres
e anos.

Optei por reutilizar o ficheiro CSS da aplicação “escola” no “portfolio”, garantindo consistência visual e evitando duplicação de código. 
Esta abordagem permite uma manutenção mais simples e uma identidade visual uniforme em toda a aplicação.

Após implementar o CRUD para a entidade Projeto, reutilizei o mesmo padrão para Tecnologia, Competência e Formação, 
o que demonstrou a consistência e reutilização de código proporcionada pelo Django através de ModelForms e views estruturadas.

Durante a implementação do CRUD, surgiram erros relacionados com templates, especialmente nas parte da edição. Este problema ocorreu porque as views estavam corretamente definidas, mas os ficheiros HTML correspondentes não tinham sido criados.
Depois que criei todos, tudo funcionou corretamente

