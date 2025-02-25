from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),  # Página inicial com lista de produtos
    path('produto/<int:produto_id>/', views.detalhe_produto, name='detalhe_produto'),  # Detalhes do produto
    path('carrinho/', views.carrinho, name='carrinho'),  # Página do carrinho
    path('carrinho/adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),  # Adiciona ao carrinho
    path('comprar/<int:produto_id>/', views.comprar, name='comprar'),  # Página de compra
]
