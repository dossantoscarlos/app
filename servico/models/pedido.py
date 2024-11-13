from django.db import models

from servico.models.cliente import Cliente
from servico.models.cupom import Cupom

class TipoStatusPedido(models.Model):
    slug = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.slug


class FormaPagamento(models.Model):
    slug = models.CharField(max_length=255)
    descricao= models.CharField(max_length=255)
    
    def __str__(self):
        return self.slug


class Pedido(models.Model):
    cupom_id = models.ForeignKey(Cupom, on_delete=models.RESTRICT)
    forma_pagamento_id = models.ForeignKey(FormaPagamento, on_delete=models.RESTRICT)
    cliente_id= models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    tipo_status_pedido_id = models.ForeignKey(TipoStatusPedido,on_delete=models.RESTRICT) 
    total_final = models.DecimalField("Total final", decimal_places=2, max_digits=10)
    valor_pago = models.DecimalField("Valor pago", decimal_places=2, max_digits=10)
    valor_restante = models.DecimalField("Valor restante", decimal_places=2, max_digits=10)
    
    def __str__(self):
        return self.total_final
