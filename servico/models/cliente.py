from django.db import models


class Cliente (models.Model):
    nome = models.CharField('Nome', max_length=255)
    fone = models.CharField('Telefone', max_length=20)
    email = models.EmailField('Email')
    
    def __str__(self):
        return self.nome
    