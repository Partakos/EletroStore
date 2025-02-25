from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='produtos/')
    
    def __str__(self):
        return self.nome

class Carrinho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade}"
