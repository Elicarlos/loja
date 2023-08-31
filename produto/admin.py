from django.contrib import admin
from .models import Categoria, Produto, Promocao, Cor, Tamanho, Subcategoria, ItemEspecial
admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Promocao)
admin.site.register(Cor)
admin.site.register(Tamanho)
admin.site.register(Subcategoria)
admin.site.register(ItemEspecial)

