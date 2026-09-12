from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['tarea', 'completada', 'fecha_limite']

        widgets = {
            'fecha_limite': forms.DateInput(attrs={'type': 'date'})
        }