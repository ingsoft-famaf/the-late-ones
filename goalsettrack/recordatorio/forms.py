from django import forms

from recordatorio.models import Recordatorio


class RecordatorioFormulario(forms.ModelForm):

    class Meta:
        model = Recordatorio
        exclude = ('meta',)
        fields = '__all__'