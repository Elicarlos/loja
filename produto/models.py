from datetime import timedelta, timezone
from django.db import models
from django.forms import ValidationError
from django.utils.text import slugify


class Tamanho(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome

class Cor(models.Model):
    cor = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.cor
    
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Subcategoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    categoria_principal = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.SET_NULL, null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.PositiveIntegerField(default=0)
    marca = models.CharField(max_length=100)
    preco_desconto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    max_imagens = models.PositiveIntegerField(default=5)
    tamanhos_disponiveis = models.ManyToManyField(Tamanho, blank=True, related_name='produtos')
    cores_disponiveis = models.ManyToManyField(Cor, blank=True, related_name='produtos')
    disponibilidade = models.BooleanField(default=True, verbose_name="Em estoque") 
    vendido = models.BooleanField(default=False, verbose_name="Vendido")
    imagem_principal = models.ImageField(upload_to='produto_imagens')
    imagem_adicional_1 = models.ImageField(upload_to='produto_imagens', blank=True)
    imagem_adicional_2 = models.ImageField(upload_to='produto_imagens', blank=True)
    imagem_adicional_3 = models.ImageField(upload_to='produto_imagens', blank=True)
    imagem_adicional_4 = models.ImageField(upload_to='produto_imagens', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, max_length=255, editable=False)

    def __str__(self):
        return self.nome
    
    def produtos_relacionados(self):
        return Produto.objects.filter(categoria_principal=self.categoria_principal).exclude(id=self.id)[:4]
    
    def clean(self):
        if not self.imagem_principal:
            raise ValidationError("É necessário fornecer uma imagem principal.")
        # if not self.imagens_adicionais.exists():
        #     raise ValidationError("É necessário fornecer pelo menos uma imagem adicional.")

    def is_new(self):
        now = timezone.now()
        return (now - self.created_at <= timedelta(days=7)) and (now - self.updated_at <= timedelta(days=7))
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

class Promocao(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=True, null=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, blank=True, null=True)
    desconto_percentual = models.DecimalField(max_digits=5, decimal_places=2)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    
    def __str__(self):
        return self.nome
