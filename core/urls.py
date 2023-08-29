from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('loja/', views.loja, name='loja')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)