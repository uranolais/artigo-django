from django.urls import path
from . import views

urlpatterns = [
    path('lista_de_livros/', views.lista_de_livros, name='lista_de_livros'),
]
