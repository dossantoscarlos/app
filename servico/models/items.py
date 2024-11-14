from django.db import models



class TipoItem (models.Model):
    slug = models.SlugField(max_length=255)
    descricao = models.CharField(verbose_name='Descrição', max_length=255)
    
    def __str__(self):
        return self.slug

class Item(models.Model): 
    tipo_item_id= models.ForeignKey(TipoItem, on_delete=models.RESTRICT)
    nome = models.CharField(verbose_name='Nome', max_length=255)
    descricao = models.TextField(verbose_name='Descrição')
    preco = models.DecimalField(verbose_name='Preço', decimal_places=2, max_digits=10)

    def __str__(self):
        return self.nome
    