from django.contrib import admin
from .models import Encomenda, ItemEncomenda

class ItemEncomendaInline(admin.TabularInline):
    model = ItemEncomenda
    extra = 0  # Para não adicionar campos extras por padrão

class EncomendaAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'estado', 'data')
    list_filter = ('estado', 'user')
    search_fields = ('user__username', 'id')
    inlines = [ItemEncomendaInline]
    
    def get_queryset(self, request):
        # Garantir que o admin possa ver todas as encomendas
        queryset = super().get_queryset(request)
        return queryset

admin.site.register(Encomenda, EncomendaAdmin)
