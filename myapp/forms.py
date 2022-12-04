from django import forms

# creating a form


class GeeksForm(forms.Form):
    geeks_field = forms.URLField(label='', required=False)


class WordForm(forms.Form):
    word_field = forms.CharField(label='', required=False)
