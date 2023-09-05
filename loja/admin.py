from django.contrib import admin
from .models import Livro

class LivroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'descricao')  # Define os campos a serem exibidos na lista

# Registra o modelo Livro com a classe LivroAdmin
admin.site.register(Livro, LivroAdmin)
