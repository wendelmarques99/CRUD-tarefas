from django.forms import ModelForm
from mycrud.models import Tarefas
from django import forms

# Create the form class.
class TarefasForm(ModelForm):
    class Meta:
        model = Tarefas
        fields = ['tarefa', 'dia', 'status']
        widgets = {
            'tarefa': forms.TextInput(attrs={'placeholder': 'Tarefa'}),
            'dia': forms.TextInput(attrs={'placeholder': 'Data'}),
            'status': forms.TextInput(attrs={'placeholder': 'Status'})
        }