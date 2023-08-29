from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('loja/', views.loja, name='loja')
]