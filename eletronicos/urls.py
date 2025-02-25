from django.urls import path
from .views import lista_produtos, detalhe_produto

urlpatterns = [
    path('', lista_produtos, name='lista_produtos'),
    path('produto/<int:produto_id>/', detalhe_produto, name='detalhe_produto'),
]
