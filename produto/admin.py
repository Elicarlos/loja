from django.contrib import admin
from .models import Categoria, Produto, Promocao, Cor, Tamanho, Subcategoria

admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Promocao)
admin.site.register(Cor)
admin.site.register(Tamanho)
admin.site.register(Subcategoria)

