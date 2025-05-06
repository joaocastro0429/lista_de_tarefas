from django.contrib import admin
from .models import Tarefa

# Register your models here.
from django.contrib import admin
from .models import Tarefa

# Register your models here.
@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'status')
    search_fields = ('titulo',)  # CORRETO: isso é uma tupla com uma vírgula
