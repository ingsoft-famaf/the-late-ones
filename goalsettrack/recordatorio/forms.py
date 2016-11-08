from django import forms

from recordatorio.models import Recordatorio


class RecordatorioFormulario(forms.Form):
    titulo = forms.CharField(max_length=80)
    mensaje = forms.CharField(max_length=80)
    fecha = forms.DateField()
    hora = forms.TimeField()
    tiempo_repeticion = forms.TimeField()

