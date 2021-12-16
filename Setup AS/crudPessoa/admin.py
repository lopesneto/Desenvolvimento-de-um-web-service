from django.contrib import admin
from crudPessoa.models import Pessoa
# Register your models here.

class Pessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'idade')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)

admin.site.register(Pessoa, Pessoas)