from django.contrib import admin

from .models import Currency


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'rate',
        'published_date',
    ]
    search_fields = ['name']
