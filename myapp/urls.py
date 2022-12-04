from django.urls import path
from . import views

urlpatterns = [
    path('top/', views.top, name='top'),
    path('upload/', views.upload, name='upload'),
    path('', views.input_url, name='input_url'),
]
