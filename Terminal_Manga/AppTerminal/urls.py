from django.urls import path
from AppTerminal import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('Mangas/', views.Mangas, name="Mangas"),
    path('Vendedores/', views.Vendedores, name="Vendedores"),
    path('Usuarios/', views.Usuarios, name="Usuarios"),
    path('mangas-formulario/', views.mangas_formulario, name="MangasFormulario"),
    path('form-con-api/', views.form_con_api, name="FormConApi")
]
