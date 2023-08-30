from django.shortcuts import render
from produto.models import Produto, Categoria

# Create your views here.


def home(request):
    produtos = Produto.objects.all()
    categoria = Categoria.objects.all()
    context = {
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
