from django.shortcuts import render
from produto.models import Produto, Categoria, ItemEspecial
from django.utils import timezone

# Create your views here.


def home(request):
    produtos = Produto.objects.all()
    categoria = Categoria.objects.all()
    tendencias = Produto.objects.filter(itemespecial__motivo='Tendencias', itemespecial__data_inicio__lte=timezone.now(), itemespecial__data_fim__gte=timezone.now())[:3]
    mais_vendidos = Produto.objects.filter(itemespecial__motivo='Best Seller', itemespecial__data_inicio__lte=timezone.now(), itemespecial__data_fim__gte=timezone.now())[:3]
    destaques = Produto.objects.filter(itemespecial__motivo='Feature', itemespecial__data_inicio__lte=timezone.now(), itemespecial__data_fim__gte=timezone.now())[:3]

       
    context = {
        'produto_tendencias': tendencias,
        'produto_mais_vendidos': mais_vendidos,
        'produto_destaques': destaques,
        'produtos': produtos,
        'categoria': categoria
    }
    return render(request, 'core/home.html', context)


def loja(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request,'shop.html', context )
