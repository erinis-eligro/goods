from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_list, name='input_list')
]