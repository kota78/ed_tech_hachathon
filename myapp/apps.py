from django.apps import AppConfig
from django import forms


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'


# creating a form
class GeeksForm(forms.Form):
    geeks_field = forms.URLField()
