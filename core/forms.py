from django import forms

from core.models import DataLoad


class LoadForm(forms.ModelForm):
    class Meta:
        model = DataLoad
        fields = ('file', )
