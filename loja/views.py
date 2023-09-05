from django.shortcuts import render
from .models import Livro

def lista_de_livros(request):
    livros = Livro.objects.all()
    return render(request, 'loja/lista_de_livros.html', {'livros': livros})
