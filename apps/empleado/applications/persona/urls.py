from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('listar-todo-empleados/', views.ListAllEmployees.as_view()),
]
