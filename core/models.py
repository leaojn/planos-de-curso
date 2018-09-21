from django.contrib.auth import get_user_model
from django.db import models
from ckeditor.fields import RichTextField
User = get_user_model()


class Professor(models.Model):
    nome = models.CharField(max_length=50, blank=False, )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Professor(a)'
        verbose_name_plural = 'Professores'


# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=50, blank=True, )
    coordenador = models.ForeignKey(Professor, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'


class Disciplina(models.Model):
    nome = models.CharField(max_length=50, blank=False, )
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    modulo = models.CharField(max_length=50, blank=False, )
    carga_horaria = models.CharField(max_length=50, blank=False, )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'


class DisciplinaProfessor(models.Model):
    disciplina = models.ForeignKey(Disciplina, blank=False, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, related_name="disciplinas", on_delete=models.CASCADE)
    semestre = models.CharField(max_length=50, blank=False, )
    ano = models.CharField(max_length=50, blank=False, )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.disciplina.nome

    class Meta:
        verbose_name = 'Disciplina e Professor'
        verbose_name_plural = 'Disciplinas e Professores'


class PlanoDisciplina(models.Model):
    disciplinaProfessor = models.ForeignKey(DisciplinaProfessor, blank=False, verbose_name='Disciplina Ministrada',on_delete=models.CASCADE)
    ementa = RichTextField(verbose_name="Ementa",)
    objetivos_gerais = RichTextField(verbose_name="Objetivos Gerais da Disciplina",)
    objetivos_especificos = RichTextField(verbose_name="Objetivos Especficos da Disciplina",)
    conteudo_programatico = RichTextField(verbose_name="Conteúdo Programático",)
    metodologia = RichTextField(verbose_name="Metologia",)
    recursos_didaticos = RichTextField(verbose_name="Recursos Didáticos",)
    sistema_de_avaliacao = RichTextField(verbose_name="Sistema de Avaliação",)
    referencias_basicas = RichTextField(verbose_name="Referências Básicas",)
    referencias_complementares = RichTextField(verbose_name="Referências Complementares",)


    def __str__(self):
        return self.disciplinaProfessor.__str__()

    class Meta:
        verbose_name = 'Plano de Disciplina'
        verbose_name_plural = 'Planos de Disciplina'


class ObjetivosEspecificos(models.Model):
    text = RichTextField(verbose_name="topicos",)
    plano = models.ForeignKey(PlanoDisciplina, related_name="objetivos"
                              , blank=False, on_delete=models.CASCADE)


class Bimestre(models.Model):
    nome_bimestre = models.CharField(verbose_name="Bimestre", max_length=50)
    plano = models.ForeignKey(PlanoDisciplina, related_name="bime"
                              , blank=False, on_delete=models.CASCADE)


class Topico(models.Model):
    texto = models.CharField(verbose_name="texto", max_length=50)
    bimestre = models.ForeignKey(Bimestre, on_delete=models.CASCADE)
    plano = models.ForeignKey(PlanoDisciplina, related_name="bimestres"
                              , blank=False, on_delete=models.CASCADE)


class ConteudoProgramatico(models.Model):
    sub = models.ForeignKey(Bimestre, on_delete=models.CASCADE)
    plano = models.ForeignKey(PlanoDisciplina, related_name="conteudo"
                              , blank=False, on_delete=models.CASCADE)
