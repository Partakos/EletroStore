from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Carrinho

# Lista todos os produtos
def lista_produtos(request):
    produtos = Produto.objects.all()  # Obtém todos os produtos do banco de dados
    return render(request, 'eletronicos/lista_produtos.html', {'produtos': produtos})

# Detalhe do produto
def detalhe_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'eletronicos/detalhe_produto.html', {'produto': produto})

# Adiciona o produto ao carrinho
def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    carrinho, created = Carrinho.objects.get_or_create(produto=produto)  # Cria o item no carrinho se não existir
    carrinho.quantidade += 1  # Aumenta a quantidade do produto no carrinho
    carrinho.save()
    return redirect('carrinho')  # Redireciona para a página do carrinho

# Exibe os produtos no carrinho
def carrinho(request):
    carrinho_itens = Carrinho.objects.all()  # Aqui você pode filtrar para mostrar o carrinho do usuário
    return render(request, 'eletronicos/carrinho.html', {'itens': carrinho_itens})

# Lógica de compra (exemplo simples)
def comprar(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    # Lógica para compra do produto (gerar pedido, confirmar pagamento, etc.)
    return render(request, 'eletronicos/compra_confirmada.html', {'produto': produto})
