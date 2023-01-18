from django.db import models

# Create your models here.
class Tarefas(models.Model):
    tarefa = models.CharField(max_length=150)
    dia = models.CharField(max_length=10)
    status = models.CharField(max_length=20)

