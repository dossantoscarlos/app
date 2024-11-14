from django.db import models
from servico.models.pedido import Pedido
from servico.models.items import Item

class ItemPedido(models.Model):    
    pedido_id = models.ForeignKey(Pedido,  on_delete= models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete= models.CASCADE)
    quantidade = models.DecimalField(decimal_places=2, max_digits=10)
    subtotal = models.DecimalField(decimal_places=2, max_digits=10)
    
    def __str__(self):
        return self.quantidade
    