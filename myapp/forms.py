from django import forms
from myapp.models import Document

# creating a form


class GeeksForm(forms.Form):
    geeks_field = forms.URLField()


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )
