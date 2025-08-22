from django.contrib import admin
from .models import Contato

# Register your models here.
admin.site.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ("nome", "telefone", "email", "criado_em")
    search_fields = ("nome", "telefone")
