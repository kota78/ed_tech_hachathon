from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_url, name='input_url'),
]
