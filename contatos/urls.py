from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_contatos, name='lista_contatos'),
    path('novo/', views.novo_contato, name='novo_contato'),
    path('editar/<int:id>/', views.editar_contato, name='editar_contato'),
    path('deletar/<int:id>/', views.deletar_contato, name='deletar_contato'),
    path('exportar-csv/', views.exportar_csv, name='exportar_csv'),
]
