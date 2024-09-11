from django.urls import path
from . import views

urlpatterns = [
    path('', views.hogar, name='hogar'),  
    path('registrar/', views.registrar, name='registrar'),  
    path('listar/', views.listar, name='listar'),  
    path('estadisticas/', views.estadisticas, name='estadisticas'),  
]