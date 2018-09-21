from django.contrib import admin

from core.models import *


# Register your models here.
class ObjetivosEspecificosInline(admin.TabularInline):
    model = ObjetivosEspecificos
    fields = ['text', ]


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    fieldsets = (
        (None, {
            'fields': ('nome', 'user',)
        }),
    )


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    fieldsets = (
        (None, {
            'fields': ('nome', 'coordenador',)
        }),
    )


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    fieldsets = (
        (None, {
            'fields': ('nome', 'curso', 'modulo', 'carga_horaria')
        }),
    )


@admin.register(DisciplinaProfessor)
class DisciplinaProfessorAdmin(admin.ModelAdmin):
    list_display = ('disciplina', 'professor')
    fieldsets = (
        (None, {
            'fields': ('disciplina', 'professor', 'semestre', 'ano',)
        }),
    )


@admin.register(PlanoDisciplina)
class PlanoDisciplinaAdmin(admin.ModelAdmin):
    list_display = ('disciplinaProfessor',)

    fieldsets = (
        (None, {
            'fields': (
            'disciplinaProfessor', 'ementa', 'objetivos_gerais', 'objetivos_especificos', 'conteudo_programatico',
            'metodologia',
            'recursos_didaticos', 'sistema_de_avaliacao', 'referencias_basicas', 'referencias_complementares',)
        }),
    )
