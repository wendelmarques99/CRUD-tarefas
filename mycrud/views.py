from django.shortcuts import render, redirect
from django.http import HttpResponse
from mycrud.forms import TarefasForm
from mycrud.models import Tarefas

# Create your views here.
def home(request):
    data = {}
    data['db'] = Tarefas.objects.all()
    return render(request, "index.html", data)

def cadastro(request):
    data_cadastro = {}
    data_cadastro['form'] = TarefasForm()
    return render(request, "cadastro.html", data_cadastro)

def create(request):
    form = TarefasForm(request.POST or None)
    if form.is_valid:
        form.save()
        return redirect("home") 

def ver(request, pk):
    data = {}
    data['db'] = Tarefas.objects.get(pk = pk)
    return render(request, "ver.html", data)

def edit(request, pk):
    data = {}
    data['db'] = Tarefas.objects.get(pk = pk)
    data["form"] = TarefasForm(instance= data['db'])
    return render(request, 'cadastro.html', data)

def update(request, pk):
    data = {}
    data['db'] = Tarefas.objects.get(pk = pk)
    form = TarefasForm(request.POST or None, instance= data['db'])
    if form.is_valid():
        form.save()
        return redirect("home")

def delete(request, pk):
    db = Tarefas.objects.get(pk = pk)
    db.delete()
    return redirect("home")