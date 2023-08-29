from django.shortcuts import render
from produto.models import Produto

# Create your views here.


def home(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, 'core/home.html', context)


def loja(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request,'shop.html', context )
