from django.shortcuts import render,redirect
from .models import Tarefa

# Create your views here.


def create(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')

        Tarefa.objects.create(
            titulo=titulo,
            descricao=descricao,
            status=True # se você tiver esse campo
        )

        return redirect('/')  # ou para onde você quiser redirecionar

    return render(request, 'create.html')

def task_list(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'list.html', {'tarefas': tarefas})




def task_update(request, id):
    tarefa = Tarefa.objects.get(id=id)  # Obtendo a tarefa pelo ID
    
    if request.method == "POST":
        # Obtendo os valores do formulário
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        status = request.POST.get('status') == "on"  # Converter status de checkbox para booleano
        
        # Atualizando a tarefa
        tarefa.titulo = titulo
        tarefa.descricao = descricao
        tarefa.status = status
        tarefa.save()  # Salvando a instância atualizada
        
        # Redirecionando para a lista de tarefas (ou para a rota desejada)
        return redirect('/')  # Ajuste a URL nomeada conforme sua necessidade
    
    return render(request, 'edit.html', {'tarefa': tarefa})
    
     
     
     

def task_destroy(request,id):
    tarefa = Tarefa.objects.get(id=id)
    tarefa.delete()
    return redirect('/')  # <- CORRETO: redireciona para a lista de tarefas

    
    
    
     
