from django.db import models
from servico.models.pedido import Pedido



class TipoEntrega(models.Model):
    slug = models.SlugField(verbose_name='Slug',max_length=255)
    descricao = models.CharField(verbose_name='Descrição', max_length=255)
    
    def __str__(self):
        return self.slug


class TipoStatusEntrega(models.Model):
    slug = models.SlugField(max_length=255)
    descricao = models.CharField(verbose_name='Descrição',max_length=255)
    
    def __str__(self):
        return self.slug


class Entrega(models.Model):
    data_prevista = models.DateField(verbose_name='Data prevista')
    data_entregue = models.DateField(verbose_name='Data entregue')
    pedido_id = models.ForeignKey(Pedido, on_delete=models.RESTRICT)
    tipo_entrega = models.ForeignKey(TipoEntrega, on_delete=models.RESTRICT)
    taxa = models.DecimalField(verbose_name="Taxa", decimal_places=2, max_digits=10)
    tipo_status_entrega_id = models.ForeignKey(TipoStatusEntrega, on_delete=models.RESTRICT) 
    
    def __str__(self):
        return self.data_prevista