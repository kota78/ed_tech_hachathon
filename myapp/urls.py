from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('input_url/', views.input_url, name='input_url'),
    path('form/', views.home_view, name='home_view'),
]
