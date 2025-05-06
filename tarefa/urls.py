from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('criar/', views.create, name='criar'),   # <--- nome precisa ser 'criar'
    path('editar/<int:id>/', views.task_update, name='edit'),  # Rota para editar tarefa]
    path('excluir/<int:id>/', views.task_destroy, name='excluir'),  # <- aqui é o essencial
]