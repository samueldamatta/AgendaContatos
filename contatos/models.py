from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return self.nome

