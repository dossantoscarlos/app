from django.db import models
from django.utils.timezone import now


class Cupom(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=255)
    descricao = models.TextField(verbose_name='Descrição')
    data_validade = models.DateField('Validade')
    data_ativacao = models.DateField('Ativação', default=now)
    valor_desconto_percentual = models.FloatField(verbose_name="Desconto persentual")
    
    def __str__(self):
        return self.nome
    
     